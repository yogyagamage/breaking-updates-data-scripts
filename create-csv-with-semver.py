import os
import pandas as pd
import json

# Directory where your JSON files are located
json_files_directory = 'benchmark'

# List all JSON files in the directory
json_files = [file for file in os.listdir(json_files_directory) if file.endswith('.json')]
# Create an empty list to store extracted data
data = []

# Loop through each JSON file and extract the required fields
for file in json_files:
    with open(os.path.join(json_files_directory, file)) as json_file:
        json_data = json.load(json_file)
        breaking_commit = json_data['breakingCommit']
        version_update_type = json_data['updatedDependency']['versionUpdateType']
        failure_category = json_data['failureCategory']
        data.append((breaking_commit, version_update_type, failure_category))

# Create a pandas DataFrame with the extracted data
df = pd.DataFrame(data, columns=["breakingCommit", "versionUpdateType", "failureCategory"])

# Save the DataFrame to a CSV file
csv_file_path = 'semver.csv'
df.to_csv(csv_file_path, index=False)

print("CSV file created successfully.")
