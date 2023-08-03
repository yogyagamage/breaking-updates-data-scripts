import csv
from collections import Counter

def count_occurrences(input_file_path, output_csv_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.read().splitlines()

    line_counts = Counter(lines)

    with open(output_csv_path, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['Line', 'Occurrences'])

        for line, count in line_counts.items():
            csv_writer.writerow([line, count])

def main():
    input_file_path = "compilation-errors\compilation_errors_extracted_lines.txt"
    output_csv_path = "compilation-errors\compilation-error-count.csv"
    count_occurrences(input_file_path, output_csv_path)

if __name__ == "__main__":
    main()
