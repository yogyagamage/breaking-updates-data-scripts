import json

# Read the project names from the text file
with open('removed_repos.txt', 'r') as file:
    project_names = [line.strip() for line in file]

# Read the JSON data
with open('found_repositories.json', 'r') as file:
    data = json.load(file)

# Remove projects from the JSON data if they exist
for project_name in project_names:
    if project_name in data:
        del data[project_name]

# Write the updated JSON data back to the file
with open('data.json', 'w') as file:
    print("done")
    json.dump(data, file, indent=2)