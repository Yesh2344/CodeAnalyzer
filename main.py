import argparse
import analyzer

def main():
    parser = argparse.ArgumentParser(
        description="Analyze Python code metrics in a directory."
    )
    parser.add_argument(
        "directory", help="Path to the directory containing Python files to analyze"
    )
    args = parser.parse_args()

    results = analyzer.analyze_directory(args.directory)
    analyzer.print_metrics(results)

if __name__ == "__main__":
    main()
