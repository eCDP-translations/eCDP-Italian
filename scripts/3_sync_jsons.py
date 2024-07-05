import json
import re
import os
import sys
from collections import OrderedDict

# Usage
# python 3_sync_json_2_order_to_json_1.py -d "da ordinare" "secondo questo ordine" "in questa cartella"

def remove_comments(json_string):
    """Remove comments from the JSON string."""
    json_string = re.sub(r'//.*', '', json_string)
    json_string = "\n".join([line for line in json_string.splitlines() if line.strip()])
    return json_string

def load_json_from_string(json_string):
    """Load JSON data from a string after removing comments."""
    cleaned_json_string = remove_comments(json_string)
    return json.loads(cleaned_json_string, object_pairs_hook=OrderedDict)
    

def order_dict_like_reference(ref_dict, target_dict):
    """Order target_dict based on the order of keys in ref_dict."""
    return OrderedDict((key, ref_dict.get(key, "")) for key in target_dict.keys())

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
        print("Usage: python script.py [-d] <source1> <source2> <output_folder>")
        sys.exit(1)

    option = sys.argv[1]
    output_folder = sys.argv[-1]

    os.makedirs(output_folder, exist_ok=True)

    if option == '-d':
        dir1 = sys.argv[2]
        dir2 = sys.argv[3]
        process_directories(dir1, dir2, output_folder)
    else:
        file_pairs = [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv) - 1, 2)]
        process_files(file_pairs, output_folder)
