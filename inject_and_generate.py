#!/usr/bin/env python3
"""
inject_and_generate.py
======================
Automates two tasks across all curriculum_pathway/ notebooks:

1. **Reading injection** — Prepends a "📖 Required Reading / Video" markdown
   cell to every lesson notebook (idempotent; skips if already present).

2. **Companion practice generation** — Creates a lightweight
   ``{name}_practice.ipynb`` companion for every tutorial notebook that
   doesn't already have one.

Usage
-----
    python inject_and_generate.py          # default: ./curriculum_pathway
    python inject_and_generate.py --dry-run  # preview without writing
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import warnings
from pathlib import Path
from typing import Dict, List, Tuple

import nbformat
from nbformat.v4 import new_markdown_cell, new_code_cell, new_notebook

# Suppress missing-id warnings from older notebooks
warnings.filterwarnings("ignore", message="Cell is missing an id field")
# Ensure Unicode prints work on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CURRICULUM_DIR = Path(__file__).parent / "curriculum_pathway"
GUIDE_FILE = CURRICULUM_DIR / "curriculum_guide.md"

READING_MARKER = "📖 Required Reading"  # idempotency sentinel

SKIP_PREFIXES = ("99_",)
SKIP_NAMES = {"00_crash_course_notes.ipynb"}
PRACTICE_KEYWORD = "practice"

# Section directories in order
SECTION_DIRS = sorted(
    [d for d in CURRICULUM_DIR.iterdir() if d.is_dir()],
    key=lambda p: p.name,
)

# ---------------------------------------------------------------------------
# 1. Parse curriculum_guide.md → reading map
# ---------------------------------------------------------------------------

ReadingMap = Dict[str, Dict[str, str]]


def parse_curriculum_guide(guide_path: Path) -> ReadingMap:
    """Return ``{section_dir_name: {lesson_num: reading_text}}``."""

    text = guide_path.read_text(encoding="utf-8")
    reading_map: ReadingMap = {}

    # Regex: section header like  ### 📁 [00_prerequisites/](...) or ### 📁 00_prerequisites/
    section_re = re.compile(
        r"###\s+📁\s+\[?(\d{2}_[a-z_]+)/?\]?"
    )
    # Regex: lesson line like  * **Lesson 03:** `03_tools_matplotlib.ipynb`
    lesson_re = re.compile(
        r"\*\s+\*\*Lesson\s+(\d{2})"
    )
    # Regex: reading line like    * 📖 **Reading**: ...
    reading_re = re.compile(
        r"\s+\*\s+📖\s+\*\*Reading\*\*:\s*(.*)"
    )

    current_section: str | None = None
    current_lesson: str | None = None

    for line in text.splitlines():
        sm = section_re.search(line)
        if sm:
            current_section = sm.group(1).rstrip("/")
            if current_section not in reading_map:
                reading_map[current_section] = {}
            current_lesson = None
            continue

        lm = lesson_re.search(line)
        if lm:
            current_lesson = lm.group(1)
            continue

        rm = reading_re.search(line)
        if rm and current_section and current_lesson:
            reading_map[current_section][current_lesson] = rm.group(1).strip()
            current_lesson = None  # consumed

    return reading_map


def _find_section_key(section_dir_name: str, reading_map: ReadingMap) -> str | None:
    """Fuzzy-match a filesystem section dir to a reading_map key.

    Handles cases like ``07_support_vector_machines`` vs ``07_svm`` by
    matching on the leading number prefix.
    """
    prefix = section_dir_name[:2]
    for key in reading_map:
        if key[:2] == prefix:
            return key
    return None


def _get_reading(
    section_dir_name: str,
    notebook_name: str,
    reading_map: ReadingMap,
) -> str:
    """Return the reading text for a given notebook, or a fallback."""

    section_key = _find_section_key(section_dir_name, reading_map)
    if section_key is None:
        return _fallback_reading()

    lesson_num = notebook_name[:2]
    section_readings = reading_map.get(section_key, {})
    reading = section_readings.get(lesson_num)
    if reading:
        return reading
    return _fallback_reading()


def _fallback_reading() -> str:
    return (
        "*No specific reading assigned. "
        "Review the section's crash course notes before proceeding.*"
    )


# ---------------------------------------------------------------------------
# 2. Inject reading cells
# ---------------------------------------------------------------------------


def _has_reading_cell(nb: nbformat.NotebookNode) -> bool:
    """Check whether the first cell already has the reading marker."""
    if nb.cells and nb.cells[0].cell_type == "markdown":
        return READING_MARKER in nb.cells[0].source
    return False


def _strip_bold(text: str) -> str:
    """Remove leading/trailing ** so we don't get ****double bold****."""
    text = text.strip()
    while text.startswith("**"):
        text = text[2:]
    while text.endswith("**"):
        text = text[:-2]
    return text.strip()


def _make_reading_cell(reading_text: str) -> nbformat.NotebookNode:
    clean = _strip_bold(reading_text)
    source = f"### {READING_MARKER} / Video\n**{clean}**"
    return new_markdown_cell(source=source)


def inject_reading_cells(
    reading_map: ReadingMap,
    dry_run: bool = False,
) -> List[str]:
    """Inject reading cells into all lesson notebooks. Returns log lines."""

    log: List[str] = []

    for section_dir in SECTION_DIRS:
        notebooks = sorted(section_dir.glob("*.ipynb"))
        for nb_path in notebooks:
            name = nb_path.name

            # Skip practice_100 and non-notebook files
            if name.startswith(SKIP_PREFIXES):
                continue

            nb = nbformat.read(str(nb_path), as_version=4)

            if _has_reading_cell(nb):
                log.append(f"[SKIP]     {section_dir.name}/{name}  (already has reading cell)")
                continue

            reading = _get_reading(section_dir.name, name, reading_map)
            cell = _make_reading_cell(reading)
            nb.cells.insert(0, cell)

            if not dry_run:
                nbformat.write(nb, str(nb_path))

            log.append(f"[INJECT]   {section_dir.name}/{name}")

    return log


# ---------------------------------------------------------------------------
# 3. Generate companion practice notebooks
# ---------------------------------------------------------------------------


def _should_generate_companion(nb_name: str) -> bool:
    """Decide whether a notebook qualifies for a companion."""
    if nb_name.startswith(SKIP_PREFIXES):
        return False
    if nb_name in SKIP_NAMES:
        return False
    if PRACTICE_KEYWORD in nb_name.lower():
        return False
    if not nb_name.endswith(".ipynb"):
        return False
    return True


def _extract_title(nb: nbformat.NotebookNode, fallback: str) -> str:
    """Try to pull the first markdown heading from the notebook."""
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # Skip the entire reading cell we injected
            if READING_MARKER in cell.source:
                continue
            for line in cell.source.splitlines():
                stripped = line.lstrip("#").strip()
                if stripped:
                    return stripped
    return fallback


def _make_companion(
    original_name: str,
    title: str,
    reading_text: str,
) -> nbformat.NotebookNode:
    """Create a companion practice notebook."""

    clean_reading = _strip_bold(reading_text)
    cells = [
        new_markdown_cell(
            source=f"### {READING_MARKER} / Video\n**{clean_reading}**"
        ),
        new_markdown_cell(
            source=(
                f"# 🏋️ Practice: {title}\n\n"
                f"Follow along with [{original_name}](./{original_name}) "
                f"and implement the key concepts from scratch."
            )
        ),
        new_markdown_cell(source="## Your Implementation"),
        new_code_cell(
            source=(
                "# YOUR CODE HERE\n"
                "# Open the original notebook side-by-side and type out the code yourself.\n"
                "# Do NOT copy-paste."
            )
        ),
    ]

    nb = new_notebook(cells=cells)
    nb.metadata.update(
        {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0",
            },
        }
    )
    return nb


def generate_companions(
    reading_map: ReadingMap,
    dry_run: bool = False,
) -> List[str]:
    """Generate companion practice notebooks. Returns log lines."""

    log: List[str] = []

    for section_dir in SECTION_DIRS:
        notebooks = sorted(section_dir.glob("*.ipynb"))
        for nb_path in notebooks:
            name = nb_path.name

            if not _should_generate_companion(name):
                continue

            stem = nb_path.stem
            companion_name = f"{stem}_practice.ipynb"
            companion_path = section_dir / companion_name

            if companion_path.exists():
                log.append(
                    f"[SKIP]     {section_dir.name}/{companion_name}  (already exists)"
                )
                continue

            # Read original to extract title
            orig_nb = nbformat.read(str(nb_path), as_version=4)
            title = _extract_title(orig_nb, stem.replace("_", " ").title())
            reading = _get_reading(section_dir.name, name, reading_map)

            companion_nb = _make_companion(name, title, reading)

            if not dry_run:
                nbformat.write(companion_nb, str(companion_path))

            log.append(f"[GENERATE] {section_dir.name}/{companion_name}")

    return log


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inject reading cells & generate companion practice notebooks."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing any files.",
    )
    args = parser.parse_args()

    if not GUIDE_FILE.exists():
        print(f"ERROR: curriculum guide not found at {GUIDE_FILE}", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("  Notebook Reading Injection & Companion Generator")
    print("=" * 60)
    if args.dry_run:
        print("  *** DRY-RUN MODE — no files will be written ***\n")

    # Step 1: Parse guide
    reading_map = parse_curriculum_guide(GUIDE_FILE)
    total_readings = sum(len(v) for v in reading_map.values())
    print(f"Parsed {len(reading_map)} sections, {total_readings} reading entries.\n")

    # Step 2: Inject reading cells
    print("-" * 60)
    print("Phase 1: Injecting reading cells")
    print("-" * 60)
    inject_log = inject_reading_cells(reading_map, dry_run=args.dry_run)
    for line in inject_log:
        print(f"  {line}")

    injected = sum(1 for l in inject_log if l.startswith("[INJECT]"))
    skipped_inject = sum(1 for l in inject_log if l.startswith("[SKIP]"))
    print(f"\n  -> Injected: {injected}  |  Skipped: {skipped_inject}\n")

    # Step 3: Generate companions
    print("-" * 60)
    print("Phase 2: Generating companion practice notebooks")
    print("-" * 60)
    companion_log = generate_companions(reading_map, dry_run=args.dry_run)
    for line in companion_log:
        print(f"  {line}")

    generated = sum(1 for l in companion_log if l.startswith("[GENERATE]"))
    skipped_gen = sum(1 for l in companion_log if l.startswith("[SKIP]"))
    print(f"\n  -> Generated: {generated}  |  Skipped: {skipped_gen}\n")

    # Summary
    print("=" * 60)
    print(f"  TOTAL: {injected} injections, {generated} companions created.")
    if args.dry_run:
        print("  (Dry run — no files were actually modified.)")
    print("=" * 60)


if __name__ == "__main__":
    main()
