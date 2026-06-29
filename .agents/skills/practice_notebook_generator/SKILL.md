---
name: practice-notebook-generator
description: >-
  Generates high-quality practice notebooks that mirror the exact header structure of parent lesson notebooks. Pulls context from textbooks or internal knowledge to insert unique practice questions for each section.
---

# Practice Notebook Generator

## Overview
Generates high-quality, individualized practice notebooks that exactly mirror the header structure of a parent lesson notebook. It pulls context from textbooks or internal knowledge to brainstorm unique practice questions for each section.

## Quick Start
- "Create the practice notebook for 01_tools_numpy.ipynb"
- "Generate practice notebooks for the entire 02_regression unit."

## Dependencies
- read_file
- run_command
- write_to_file

## Workflow

### 1. Gather Context
- Read `curriculum_guide.md` (or similar syllabus) to determine the exact textbook/chapter mapping for the requested notebook(s).
- Attempt to read the corresponding textbook file from the workspace (if provided) to gather highly relevant context. If the file is not found, **first** ask the user to provide it. If they prefer not to, fall back to your internal knowledge of standard ML books (e.g., HOML3, ISLP).

### 2. Brainstorm Questions
- Read the target parent notebook(s) using the `read_file` or `view_file` tool to extract the exact Markdown headers (`#`, `##`, etc.).
- For each header, use the textbook context and your internal ML knowledge to write a unique, high-quality coding practice question or task.
- Format these questions as a single JSON object where the key is the exact header text (without the `#`) and the value is the practice question string.

### 3. Save JSON Mapping
- Write the JSON object to a temporary file (e.g., `questions_tmp.json`) in the workspace scratch directory using `write_to_file`.

### 4. Build Notebook
- Run the helper script located in this skill directory to generate the `.ipynb` file.
  `python .agents/skills/practice_notebook_generator/scripts/create_practice_nb.py build --target <path_to_parent_notebook> --questions-json <path_to_temp_json> --output <path_to_new_practice_notebook>`
- The script will read the target, insert the questions under the respective headers, add empty `# YOUR CODE HERE` cells, and write the output.

### 5. Loop (If batch processing)
- If generating for an entire unit, repeat steps 2-4 for each notebook individually to maintain high quality and avoid overwhelming the context window. Do not try to generate hundreds of questions at once.

## Utility Scripts
**`create_practice_nb.py`**
A CLI script that takes the original notebook, strips the explanatory text and completed code, and inserts the generated questions under the exact matching headers.

Example:
```bash
python .agents/skills/practice_notebook_generator/scripts/create_practice_nb.py build --target 01_tools_numpy.ipynb --questions-json questions.json --output 01_tools_numpy_practice.ipynb
```

## Common Mistakes
- **Overwriting the parent notebook**: Ensure the `--output` flag always points to a new file named `_practice.ipynb`.
- **Malformed JSON**: Ensure the questions are saved as valid JSON before passing to the helper script.
- **Missing headers**: The keys in the JSON must closely match the text of the headers in the parent notebook (though the script supports fuzzy matching).
