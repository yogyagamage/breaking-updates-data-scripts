import os
import json
import csv

# Function to process a single JSON file
def process_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Extract relevant data from the JSON
    dependency_group_id = data["updatedDependency"]["dependencyGroupID"]
    dependency_artifact_id = data["updatedDependency"]["dependencyArtifactID"]
    project = data["project"]

    return dependency_group_id, dependency_artifact_id, project, os.path.basename(file_path)

# Directory where your JSON files are located
json_files_dir = 'C:\\Users\\Yogya\\Documents\\KTH\\Breaking Updates\\breaking-updates\\data\\benchmark'

# Dictionary to store the data
dependency_data = {}

# Loop through each JSON file in the directory
for file_name in os.listdir(json_files_dir):
    if file_name.endswith('.json'):
        file_path = os.path.join(json_files_dir, file_name)
        dependency_group_id, dependency_artifact_id, project, file_name = process_json_file(file_path)

        # Store the data in the dictionary
        key = (dependency_group_id, dependency_artifact_id)
        if key not in dependency_data:
            dependency_data[key] = []
        dependency_data[key].append((project, file_name))

# Print the unique combinations of dependencyGroupID and dependencyArtifactID with their corresponding filenames and projects
with open("group-dependencies\\grouped-dependencies.txt", "w") as text_file:
    for key, values in dependency_data.items():
        dependency_group_id, dependency_artifact_id = key
        text_file.write(f"Dependency Group ID: {dependency_group_id}, Dependency Artifact ID: {dependency_artifact_id}")
        text_file.write('\n')
        for project, file_name in values:
            text_file.write(f"  Project: {project}, File Name: {file_name}")
            text_file.write('\n')
        text_file.write('\n')  # Add a newline for readability


dependency_data_csv = {}

# Loop through each JSON file in the directory
for file_name in os.listdir(json_files_dir):
    if file_name.endswith('.json'):
        file_path = os.path.join(json_files_dir, file_name)
        dependency_group_id, dependency_artifact_id, project, file_name = process_json_file(file_path)

        # Store the data in the dictionary
        key = (dependency_group_id, dependency_artifact_id)
        if key not in dependency_data_csv:
            dependency_data_csv[key] = {'projects': set(), 'files': []}
        dependency_data_csv[key]['projects'].add(project)
        dependency_data_csv[key]['files'].append(file_name)


# Write the data to a CSV file
output_file = 'group-dependencies\\grouped-dependencies.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Dependency Group ID', 'Dependency Artifact ID', 'Number of Unique Projects', 'Number of Total Files']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for key, values in dependency_data_csv.items():
        dependency_group_id, dependency_artifact_id = key
        num_unique_projects = len(values['projects'])
        num_total_files = len(values['files'])
        writer.writerow({
            'Dependency Group ID': dependency_group_id,
            'Dependency Artifact ID': dependency_artifact_id,
            'Number of Unique Projects': num_unique_projects,
            'Number of Total Files': num_total_files
        })

