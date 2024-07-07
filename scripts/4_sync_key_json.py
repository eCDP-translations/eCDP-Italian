import json
import re
import os
import sys
from collections import OrderedDict


def load_json_from_string(json_string):
    """Load JSON data from a string after removing comments."""
    return json.loads(cleaned_json_string, object_pairs_hook=OrderedDict)
    
def process_files(file_pairs, output_folder):
    for file_pair in file_pairs:
        file_1, file_2 = file_pair

        with open(file_1, 'r', encoding='utf-8') as f1, open(file_2, 'r', encoding='utf-8') as f2:
            json_string_1 = f1.read()
            json_string_2 = f2.read()

        dict_1 = load_json_from_string(json_string_1)
        dict_2 = load_json_from_string(json_string_2)

        ordered_dict_2 = order_dict_like_reference(dict_1, dict_2)

        output_filename = os.path.join(output_folder, os.path.basename(file_2))

        with open(output_filename, 'wb') as outfile:
            outfile.write(json.dumps(ordered_dict_2, ensure_ascii=False, indent=4).encode('utf-8'))

        print(f"Processed {file_2} -> {output_filename}")

def process_directories(dir1, dir2, output_folder):
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        print("Both arguments must be directories")
        sys.exit(1)

    files_dir1 = set(os.listdir(dir1))
    files_dir2 = set(os.listdir(dir2))

    common_files = files_dir1.intersection(files_dir2)
    
    file_pairs = [(os.path.join(dir1, file), os.path.join(dir2, file)) for file in common_files]

    process_files(file_pairs, output_folder)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <dir1> <dir2> <output_folder>")
        sys.exit(1)

    output_folder = sys.argv[-1]

    os.makedirs(output_folder, exist_ok=True)

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    process_directories(dir1, dir2, output_folder)
