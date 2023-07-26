import os
import json

json_files_directory = 'benchmark'
json_files = [file for file in os.listdir(json_files_directory) if file.endswith('.json')]

log_files_directory = 'C://Users//Yogya//Documents//KTH//Breaking Updates//breaking-updates//reproductionLogs//successfulReproductionLogs'
log_files = os.listdir(log_files_directory)

patterns = [
    "Failed to execute goal org.jenkins-ci.tools:maven-hpi-plugin",
    "Failed to execute goal com.carrotsearch.randomizedtesting:junit4-maven-plugin",
    "There were test failures"
]

for file in json_files:
    with open(os.path.join(json_files_directory, file), 'r') as json_file:
        json_data = json.load(json_file)
        if json_data['failureCategory'] == "UNKNOWN_FAILURE":
            log_file_name = json_data['breakingCommit'] + '.log'
            if log_file_name in log_files:
                log_file_path = os.path.join(log_files_directory, log_file_name)
                with open(log_file_path, 'r', encoding="utf8") as log_file:
                    log_content = log_file.read()
                    for pattern in patterns:
                        if pattern in log_content:
                            if pattern == patterns[0]:
                                json_data['failureCategory'] = "MAVEN_HPI_PLUGIN_FAILURE"
                            elif pattern in (patterns[1], patterns[2]):
                                json_data['failureCategory'] = "TEST_FAILURE"

    with open(os.path.join(json_files_directory, file), 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
        print(f"Updated {json_data['breakingCommit']}")
