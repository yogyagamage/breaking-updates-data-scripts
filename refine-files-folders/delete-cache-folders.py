import os
import shutil

# Specify the paths to your JSON folder and the folder with subfolders
json_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates\\data\\benchmark'
subfolder_parent = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates-cache\\data'

# Create a set to store the names of JSON files
json_files = set()

# Iterate through JSON folder and collect JSON file names
for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        json_files.add(filename.split('.')[0])

# Iterate through subfolders and delete those without corresponding JSON files
with open('deleted_subfolders.txt', 'w') as file:
    for subfolder in os.listdir(subfolder_parent):
        subfolder_path = os.path.join(subfolder_parent, subfolder)
        if os.path.isdir(subfolder_path) and subfolder not in json_files:
            print(f"Deleting subfolder: {subfolder}")
            file.write(subfolder + '\n')
            shutil.rmtree(subfolder_path)

# Create a text file with a list of <some_number> without corresponding subfolders
missing_subfolders = [name for name in json_files if not os.path.exists(os.path.join(subfolder_parent, name))]
with open('missing_subfolders.txt', 'w') as file:
    for name in missing_subfolders:
        file.write(name + '\n')
