import os
import json
import re

json_files_directory = 'C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates\\data\\benchmark'
json_files = [file for file in os.listdir(json_files_directory) if file.endswith('.json')]

pattern = r"^\d+\.\d+\.\d+$"
pattern_without_patch = r"^\d+\.\d+$"

for file in json_files:
    isUpdated = False
    with open(os.path.join(json_files_directory, file), 'r') as json_file:
        json_data = json.load(json_file)
        prev_version = json_data["updatedDependency"]["previousVersion"]
        new_version = json_data["updatedDependency"]["newVersion"]
        if ((re.match(pattern, prev_version) or re.match(pattern_without_patch, prev_version))  and 
            (re.match(pattern, new_version) or re.match(pattern_without_patch, new_version))):
            prev_version_numbers = prev_version.split(".")
            new_version_numbers = new_version.split(".")
            if (int(prev_version_numbers[0]) < int(new_version_numbers[0])):
                if (json_data["updatedDependency"]["versionUpdateType"] != "major"):
                    isUpdated = True
                    json_data["updatedDependency"]["versionUpdateType"] = "major"
            elif (int(prev_version_numbers[1]) < int(new_version_numbers[1])):
                if (json_data["updatedDependency"]["versionUpdateType"] != "minor"):
                    isUpdated = True
                    json_data["updatedDependency"]["versionUpdateType"] = "minor"
            else:
                if (json_data["updatedDependency"]["versionUpdateType"] != "patch"):
                    isUpdated = True
                    json_data["updatedDependency"]["versionUpdateType"] = "patch"
        else:
            if (json_data["updatedDependency"]["versionUpdateType"] != "other"):
                isUpdated = True
                json_data["updatedDependency"]["versionUpdateType"] = "other"
    if (isUpdated):
        with open(os.path.join(json_files_directory, file), 'w') as json_file:
            json.dump(json_data, json_file, indent=2, separators=(',', ' : '))
            print(f"Updated {json_data['breakingCommit']}") 
