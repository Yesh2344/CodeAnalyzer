import os

def count_lines(file_path):
    """Count total, code, comment, and blank lines in a Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, 0, 0, 0

    total_lines = len(lines)
    comment_lines = sum(1 for line in lines if line.strip().startswith("#"))
    blank_lines = sum(1 for line in lines if line.strip() == "")
    code_lines = total_lines - comment_lines - blank_lines
    return total_lines, code_lines, comment_lines, blank_lines

def analyze_directory(directory):
    """Recursively analyze Python files in the specified directory."""
    results = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                total, code, comments, blanks = count_lines(path)
                results[path] = {
                    "total_lines": total,
                    "code_lines": code,
                    "comment_lines": comments,
                    "blank_lines": blanks,
                }
    return results

def print_metrics(results):
    """Display metrics for each analyzed file."""
    if not results:
        print("No Python files found.")
        return

    for file, metrics in results.items():
        print(f"File: {file}")
        print(f"  Total Lines   : {metrics['total_lines']}")
        print(f"  Code Lines    : {metrics['code_lines']}")
        print(f"  Comment Lines : {metrics['comment_lines']}")
        print(f"  Blank Lines   : {metrics['blank_lines']}")
        print("-" * 40)
