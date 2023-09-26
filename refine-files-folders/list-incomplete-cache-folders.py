import os

# Specify the paths to your JSON folder and the folder with subfolders
json_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates\\data\\benchmark'
subfolder_parent = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates-cache\\data'

# Create sets to store the names of JSON files, subfolders without files
json_files = set()
subfolders_without_log = set()
subfolders_without_prev_jar = set()
subfolders_without_new_jar = set()

# Iterate through JSON folder and collect JSON file names
for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        json_files.add(filename.split('.')[0])

# Iterate through subfolders and check for files
for subfolder in os.listdir(subfolder_parent):
    subfolder_path = os.path.join(subfolder_parent, subfolder)
    
    # Check if it's a directory
    if os.path.isdir(subfolder_path):
        # Check for log file
        log_file_exists = any(filename.endswith('.log') for filename in os.listdir(subfolder_path))
        if not log_file_exists:
            subfolders_without_log.add(subfolder)

        # Check for __prev.jar file
        prev_jar_exists = any(filename.endswith('__prev.jar') for filename in os.listdir(subfolder_path))
        prev_pom_exists = any(filename.endswith('__prev.pom') for filename in os.listdir(subfolder_path))
        if not prev_jar_exists and not prev_pom_exists:
            subfolders_without_prev_jar.add(subfolder)

        # Check for __new.jar file
        new_jar_exists = any(filename.endswith('__new.jar') for filename in os.listdir(subfolder_path))
        new_pom_exists = any(filename.endswith('__new.pom') for filename in os.listdir(subfolder_path))
        if not new_jar_exists and not new_pom_exists:
            subfolders_without_new_jar.add(subfolder)

# Create text files for subfolders without log, __prev.jar, and __new.jar
with open('subfolders_without_log.txt', 'w') as file:
    for name in subfolders_without_log:
        file.write(name + '\n')

with open('subfolders_without_prev_jar.txt', 'w') as file:
    for name in subfolders_without_prev_jar:
        file.write(name + '\n')

with open('subfolders_without_new_jar.txt', 'w') as file:
    for name in subfolders_without_new_jar:
        file.write(name + '\n')
