# Python Documentation Extractor

This Python script extracts docstrings and comments from Python files in a specified folder, compiles them into a summary, and saves the result to a file.

## Features

- Extracts **docstrings** (`"""` and `'''`) and **comments** (`#`) from Python files.
- Processes all Python files in a given folder, including subfolders.
- Generates a summary of the extracted documentation and saves it to a `documentation_summary.txt` file.

## How It Works

1. **Docstring Extraction**: Collects all docstrings (`"""` and `'''`) using regular expressions.
2. **Comment Extraction**: Collects single-line comments starting with `#`.
3. **File Traversal**: Processes all `.py` files in the specified folder and its subfolders.
4. **Summary Generation**: Creates a summary with the extracted docstrings and comments for each file.
5. **Output File**: Saves the summary to `documentation_summary.txt` in the provided folder.
