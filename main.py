import os
import re

def extract_docstrings(file_path):
    """
    Extracts docstrings and comments from a Python file.
    :param file_path: Path to the Python file.
    :return: A list of extracted docstrings and comments.
    """
    docstrings = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            docstrings += re.findall(r'"""(.*?)"""', content, re.DOTALL)
            docstrings += re.findall(r"'''(.*?)'''", content, re.DOTALL)

            comments = re.findall(r'#.*', content)
            docstrings += comments

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return docstrings

def summarize_folder(folder_path):
    """
    Summarizes docstrings and comments for all Python files in a folder.
    :param folder_path: Path to the folder containing Python files.
    :return: A summary string.
    """
    summary = "Documentation Summary\n====================\n\n"
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                summary += f"File: {file}\n"
                docstrings = extract_docstrings(file_path)
                if docstrings:
                    summary += "\n".join([f"    - {line.strip()}" for line in docstrings]) + "\n"
                else:
                    summary += "    No documentation found.\n"
                summary += "\n"

    return summary

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing Python files: ")
    if os.path.isdir(folder_path):
        documentation = summarize_folder(folder_path)
        output_file = os.path.join(folder_path, "documentation_summary.txt")
        with open(output_file, 'w', encoding='utf-8') as doc_file:
            doc_file.write(documentation)
        print(f"Documentation summary saved to {output_file}")
    else:
        print("Invalid folder path.")
