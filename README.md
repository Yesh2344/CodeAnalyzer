# Python Code Metrics Analyzer

A command-line tool that analyzes Python source code files in a directory and provides detailed metrics about code composition, including counts of total lines, code lines, comments, and blank lines.

## Features

- Recursive directory scanning for Python files
- Detailed metrics for each file:
  - Total number of lines
  - Number of code lines
  - Number of comment lines
  - Number of blank lines
- UTF-8 encoding support
- Error handling for file reading issues
- Command-line interface with directory path argument

## Installation

Clone this repository:

```bash
git clone https://github.com/yesh2344/python-metrics-analyzer.git
cd python-metrics-analyzer
```

No additional dependencies are required beyond Python's standard library.

## Usage

Run the analyzer from the command line by providing a directory path:

```bash
python main.py /path/to/your/python/project
```

### Example Output

```
File: /path/to//project/example.py
  Total Lines   : 100
  Code Lines    : 75
  Comment Lines : 15
  Blank Lines   : 10
----------------------------------------
```

## Project Structure

```
python-metrics-analyzer/
├── analyzer.py       # Core analysis functionality
├── main.py          # Command-line interface
└── README.md        # Project documentation
```

## How It Works

1. The tool recursively scans the specified directory for `.py` files
2. For each Python file found, it:
   - Counts total lines in the file
   - Identifies and counts comment lines (starting with #)
   - Counts blank lines
   - Calculates actual code lines (total - comments - blanks)
3. Results are displayed in a formatted output for each file

## Contributing

Contributions are welcome! Here are some ways you can contribute:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements

- Add support for multi-line comments and docstrings
- Generate statistical summaries for entire projects
- Export results to different formats (CSV, JSON)
- Add code complexity metrics
- Support for other programming languages

## Author

Yeswanth Soma

## Acknowledgments

- Inspired by the need for simple code metrics in Python projects
- Thanks to all contributors and users of this tool

## Copryrights

All Copyrights Reserved @Yeswanth Soma
