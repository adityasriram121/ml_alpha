import sys
import json
import argparse
from pathlib import Path
import warnings

# Suppress nbformat missing id warnings for older notebooks
warnings.filterwarnings("ignore", message="Cell is missing an id field")

try:
    import nbformat
    from nbformat.v4 import new_markdown_cell, new_code_cell, new_notebook
except ImportError:
    print("Error: nbformat is not installed. Please install it with: pip install nbformat", file=sys.stderr)
    sys.exit(1)

def get_practice_prompt(header_text: str, questions: dict) -> str:
    """Find a matching question for a header, or return a generic one."""
    clean_header = header_text.lstrip("#").strip()
    
    if clean_header in questions:
        return questions[clean_header]
    
    # Fuzzy match
    for key, question in questions.items():
        if key.lower() in clean_header.lower():
            return question

    return (f"Practice Exercise for **{clean_header}**:\n"
            f"Implement a small, self-contained example demonstrating the core concept of {clean_header}. "
            f"Do not copy the original notebook code exactly; invent your own dummy data or scenario.")

def build_notebook(target_path: Path, questions_path: Path, output_path: Path):
    if not target_path.exists():
        print(f"Error: Target notebook not found: {target_path}", file=sys.stderr)
        sys.exit(1)
        
    if not questions_path.exists():
        print(f"Error: Questions JSON not found: {questions_path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(questions_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {questions_path}: {e}", file=sys.stderr)
        sys.exit(1)

    orig_nb = nbformat.read(str(target_path), as_version=4)
    new_cells = []
    
    # Title cell
    title = target_path.name.replace("_", " ").replace(".ipynb", "").title()
    new_cells.append(new_markdown_cell(f"# 🏋️ Custom Practice: {title}\n*This notebook mirrors the structure of the lesson. Complete the unique exercises for each section.*"))
    
    headers_found = 0
    
    for cell in orig_nb.cells:
        if cell.cell_type == "markdown":
            lines = cell.source.splitlines()
            if not lines:
                continue
            
            first_line = lines[0].strip()
            if first_line.startswith("#") and "Required Reading" not in first_line:
                new_cells.append(new_markdown_cell(first_line))
                prompt = get_practice_prompt(first_line, questions)
                new_cells.append(new_markdown_cell(f"**✨ Task:** {prompt}"))
                new_cells.append(new_code_cell("# YOUR CODE HERE\n"))
                headers_found += 1

    practice_nb = new_notebook(cells=new_cells)
    practice_nb.metadata = orig_nb.metadata
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(practice_nb, str(output_path))
    
    result = {
        "status": "success",
        "output_file": str(output_path.absolute()),
        "sections_generated": headers_found
    }
    
    print(f"Success! Notebook written to: {output_path}")
    # Write a metadata file for the agent to read if needed
    meta_out = output_path.with_suffix('.meta.json')
    with open(meta_out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Generate a practice notebook from a parent notebook and a JSON of questions.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    build_parser = subparsers.add_parser("build", help="Build the practice notebook")
    build_parser.add_argument("--target", required=True, help="Path to the original parent notebook")
    build_parser.add_argument("--questions-json", required=True, help="Path to a JSON file containing mapping of headers to questions")
    build_parser.add_argument("--output", required=True, help="Path where the practice notebook should be saved")
    
    args = parser.parse_args()
    
    if args.command == "build":
        build_notebook(Path(args.target), Path(args.questions_json), Path(args.output))

if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
