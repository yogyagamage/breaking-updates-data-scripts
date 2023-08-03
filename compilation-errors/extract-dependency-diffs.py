import os
import json
import re

def is_word_in_json_object(word, json_object):
    for key, value in json_object.items():
        if isinstance(value, str) and word in value:
            return True
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and is_word_in_json_object(word, item):
                    return True
    return False

def process_word(word):
    # Replace '/' with '.'
    word = word.replace('/', '.')
    # Remove characters that are not numbers, letters, '.', '-', or ':'
    word = re.sub(r'[^0-9a-zA-Z.\-:]', '', word)
    # Remove the part of the word that follows ':'
    word = word.split(':', 1)[0]
    return word

def search_log_and_json(dependency_folder, data_folder, output_file_name, log_folder):
    output_list = []
    for root, dirs, files in os.walk(dependency_folder):
        for file in files:
            if file.endswith(".json"):
                breaking_commit = file[:-5]  # Remove ".json" extension
                print('breaking commit' + breaking_commit)
                subfolder_path = os.path.join(data_folder, breaking_commit)
                try :
                    search_json_files = [f for f in os.listdir(subfolder_path) if f.endswith(".json")]
                
                    # Find the search JSON file inside the subfolder
                    if len(search_json_files) == 1:
                        print('revapi json file found')
                        search_json_path = os.path.join(subfolder_path, search_json_files[0])

                        with open(search_json_path, 'r') as search_file:
                            search_data = json.load(search_file)
                        log_files = [f for f in os.listdir(log_folder) if f.endswith(".log") and f.startswith(breaking_commit)]
                        if len(log_files) == 1:
                            print('log file found')
                            log_file_path = os.path.join(log_folder, log_files[0])
                            with open(log_file_path, 'r', encoding="ISO-8859-1") as log_file:
                                log_content = log_file.read()
                            # Search for the patterns in the log file
                            found_words = set()
                            patterns = [
                                r"package (\S+) does not exist",
                                r"cannot access (\S+)",
                                r"incompatible types: ([^\n]+) cannot be converted to ([^\n]+)",
                                r"incompatible types: ([^\n]+) is not a functional interface",
                                r"method ([^\n]+) cannot be applied to given types",
                                r"([^\n]+) has private access in ([^\n]+)",
                                r"no suitable constructor found for ([^\n]+)",
                                r"([^\n]+) is not abstract and does not override abstract method file([^\n]+)"
                            ]
                            for pattern in patterns:
                                matches = re.finditer(pattern, log_content)
                                for match in matches:
                                    for group in match.groups():
                                        if group is not None:
                                            words = group.strip().split() 
                                            for word in words:
                                                if '.' in word:
                                                    processed_word = process_word(word)
                                                    if processed_word:
                                                        found_words.add(processed_word)
                            print(found_words)
                            found_words = list(found_words)
                            if found_words:
                                for found_word in found_words:
                                    print('looking for the word - ' + found_word + ' - in revapi json file')
                                    all_objs = []
                                    # Search for the found_word in the JSON file
                                    for obj in search_data:
                                        if is_word_in_json_object(found_word, obj):
                                            print('found the word in revapi result too')
                                            all_objs.append(obj)
                                    found_word_object = {
                                        'comiplation_failure_method_found_in_log': found_word,
                                        'revapi_objects': all_objs
                                    }
                                output_data = {
                                    'breaking_commit': breaking_commit,
                                    'revapi_matching_results': found_word_object
                                }
                                output_list.append(output_data)
                except :
                    print('No folder found in cache folder for the bu')
    with open(output_file_name, 'w') as output_file:
        json.dump(output_list, output_file, indent=2)

def main():
    dependency_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates\\data\\benchmark'
    data_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates-cache\data'
    output_file_name = 'compilation-errors\\dependency-error-diffs.json'
    log_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates\\reproductionLogs\\successfulReproductionLogs'
    search_log_and_json(dependency_folder, data_folder, output_file_name, log_folder)

if __name__ == "__main__":
    main()
