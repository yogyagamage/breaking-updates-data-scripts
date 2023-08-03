import os
import json

with open('removed_repos.txt', 'r') as file:
    project_names = [line.strip() for line in file]

folder_path = "dataset"

# simple version for working with CWD
print (len([name for name in os.listdir('dataset') if os.path.isfile(name)]))

# Iterate over the files in the folder
for project_name in project_names:
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            url = data.get("url", "")
            if project_name in url:
                os.remove(file_path)
                print(f"Deleted {filename}")
print (len([name for name in os.listdir('dataset') if os.path.isfile(name)]))