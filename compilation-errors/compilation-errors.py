import os
import re

def extract_lines_between_keywords(log_file_path, output_file_path):
    start_keyword = "[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin"
    end_keyword = "[ERROR] -> [Help 1]"
    
    with open(log_file_path, 'r', encoding="utf8") as log_file:
        log_content = log_file.readlines()

    extracted_lines = []
    is_extracting = False

    for line in log_content:
        if start_keyword in line:
            is_extracting = True
            extracted_lines.append(line)
        elif end_keyword in line:
            is_extracting = False
        elif is_extracting:
            extracted_lines.append(line)
    if (len(extracted_lines) != 0):
        with open(output_file_path, 'a') as output_file:
            output_file.writelines(log_file_path)
            output_file.write('\n')
            output_file.write('\n')
            output_file.writelines(extracted_lines)
            output_file.writelines("----------------------------------------------------------------------------------------------------")
            output_file.write('\n')

def extract_lines_with_pattern(file_path):
    pattern = r"\[\d+,\d+\]\s+(.+)"  
    matching_parts = []

    with open(file_path, 'r') as file:
        content = file.readlines()

    for line in content:
        match = re.search(pattern, line)
        if match:
            matching_parts.append(match.group(1))

    return matching_parts

def remove_patterns(file_path):
    patterns_to_remove = [
        r"error: ",
        r"package \S+ does not exist",
        r"cannot access \S+",
        r"incompatible types: ([^\n]+) cannot be converted to ([^\n]+)",
        r"incompatible types: ([^\n]+) is not a functional interface",
        r"method ([^\n]+) cannot be applied to given types",
        r"([^\n]+) has private access in ([^\n]+)",
        r"no suitable constructor found for ([^\n]+)",
        r"([^\n]+) is not abstract and does not override abstract method file([^\n]+)"
    ]
    patterns_to_sub = [
        "",
        "package does not exist",
        "cannot access",
        "incompatible types: cannot be converted to",
        "incompatible types: is not a functional interface",
        "method cannot be applied to given types",
        "has private access in",
        "no suitable constructor found for",
        "is not abstract and does not override abstract method file"
    ]

    with open(file_path, 'r') as file:
        content = file.read()

    for i in range(len(patterns_to_remove)):
        content = re.sub(patterns_to_remove[i], patterns_to_sub[i], content)

    with open(file_path, 'w') as file:
        file.write(content)

def main():
    log_folder = "C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates\\reproductionLogs\\successfulReproductionLogs"
    output_file_path = "compilation-errors\compilation_errors_all.txt"
    output_file_path_lines = "compilation-errors\compilation_errors_extracted_lines.txt"

    open(output_file_path, 'w').close()
    open(output_file_path_lines, 'w').close()

    for filename in os.listdir(log_folder):
        if filename.endswith(".log"):
            log_file_path = os.path.join(log_folder, filename)
            extract_lines_between_keywords(log_file_path, output_file_path)

    extracted_lines = extract_lines_with_pattern(output_file_path)
    with open(output_file_path_lines, 'a') as output_file:
        for line in extracted_lines:
            output_file.writelines(line)
            output_file.write('\n')

    remove_patterns(output_file_path_lines)
    

if __name__ == "__main__":
    main()
