import os
import json

folder_path = "dataset"

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Remove the "type" field from the JSON data
        if "type" in data:
            del data["type"]
        
        # Write the updated JSON data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Removed 'type' field from {filename}")