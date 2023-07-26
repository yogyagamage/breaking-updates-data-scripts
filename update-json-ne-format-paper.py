import os
import json
from collections import OrderedDict

folder_path = "not-reproduced-data"

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file, object_pairs_hook=OrderedDict)
        
        # Rename the "commit" field to "breakingCommit"
        if "commit" in data:
            data["breakingCommit"] = data.pop("commit")

        # Preserve the order
        data.move_to_end("breakingCommit", last=False)
        data.move_to_end("project", last=False)
        data.move_to_end("url", last=False)
        
        # Add a new field called "updatedDependency"
        updated_dependency_fields = [
            "dependencyGroupID",
            "dependencyArtifactID",
            "previousVersion",
            "newVersion",
            "dependencyScope",
            "versionUpdateType"
        ]
        updated_dependency = OrderedDict()
        for field in updated_dependency_fields:
            if field in data:
                updated_dependency[field] = data[field]
                del data[field]
        if updated_dependency["dependencyScope"] == "unknown":
            updated_dependency["dependencyScope"] = "compile"
        data["updatedDependency"] = updated_dependency

        # Delete specific fields
        fields_to_delete = [
            "createdAt",
            "dependencyGroupID",
            "dependencyArtifactID",
            "previousVersion",
            "newVersion",
            "dependencyScope",
            "versionUpdateType",
            "baseBuildCommand",
            "breakingUpdateReproductionCommand",
            "reproductionStatus",
            "analysis",
            "metadata"
        ]
        for field in fields_to_delete:
            if field in data:
                del data[field]
        
        # Write the updated JSON data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Updated {filename}")
