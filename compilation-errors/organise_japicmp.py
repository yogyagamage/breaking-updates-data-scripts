import json
import csv
from collections import defaultdict

# Load the updated JSON data with the "project" field
with open('updated_data.json', 'r') as f:
    updated_data = json.load(f)

# Initialize a dictionary to store counts by project
result_counts_by_project = defaultdict(lambda: defaultdict(int))

# Iterate through the data and accumulate counts by project
for key, value in updated_data.items():
    project = value.get("project")
    japicmp_result = value.get("japicmpResult", {})
    
    if project:
        for item in japicmp_result:
            for result_item in japicmp_result[item]:
                result_counts_by_project[project][result_item] += 1

# Define the CSV file name
csv_file = 'project_japicmp_counts.csv'

# Write the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    header_row = ["Project", "JapicmpResult Item", "Count"]
    csv_writer.writerow(header_row)
    
    # Write the data rows
    for project, counts in result_counts_by_project.items():
        for item, count in counts.items():
            csv_writer.writerow([project, item, count])

print(f"Data written to {csv_file}.")

###########################################################

result_counts = defaultdict(int)

# Iterate through the data and accumulate counts
for key, value in updated_data.items():
    japicmp_result = value.get("japicmpResult", {})
    
    for item in japicmp_result:
        for result_item in japicmp_result[item]:
            result_counts[result_item] += 1

# Define the CSV file name
csv_file = 'japicmp_counts.csv'

# Write the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    header_row = ["JapicmpResult Item", "Count"]
    csv_writer.writerow(header_row)
    
    # Write the data rows
    for item, count in result_counts.items():
        csv_writer.writerow([item, count])

print(f"Data written to {csv_file}.")

