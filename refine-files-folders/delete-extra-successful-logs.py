import os
import shutil

# Specify the paths to your JSON folder and the folder with subfolders
json_folder = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates\\data\\benchmark'
subfolder_parent = 'C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates-cache\\data'
log_folder = "C:\\Users\\Yogya\\Documents\\KTH\\BreakingUpdates\\breaking-updates\\reproductionLogs\\successfulReproductionLogs"


json_files = [os.path.splitext(file)[0] for file in os.listdir(json_folder) if file.endswith(".json")]

# Iterate through the log files
for log_file in os.listdir(log_folder):
    if log_file.endswith(".log"):
        # Get the file name without the extension
        log_file_name = os.path.splitext(log_file)[0]
        
        # Check if a corresponding JSON file exists
        if log_file_name not in json_files:
            # Build the full path to the log file
            log_file_path = os.path.join(log_folder, log_file)
            
            # Delete the log file
            os.remove(log_file_path)
            print(f"Deleted {log_file_path}")
