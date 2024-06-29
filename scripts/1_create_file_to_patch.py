import os
import json

def is_json_dict(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return isinstance(data, dict)
    except (ValueError, json.JSONDecodeError):
        return False
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return False

with open("../files_to_remove_keys.txt", "a", encoding="utf-8") as f:
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                if not is_json_dict(filepath):
                    f.write(filepath + "\n")
