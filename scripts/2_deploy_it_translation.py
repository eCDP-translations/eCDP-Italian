import os
import json
import shutil

def is_json_dict(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return isinstance(data, dict)
    except (ValueError, json.JSONDecodeError):
        return False
    except Exception as e:
        # Log other exceptions such as permission issues
        print(f"Error reading file {filepath}: {e}")
        return False

def convert_dict_to_list(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = list(data.values())

    with open(filepath, "wb") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4).encode("utf-8"))

os.chdir("..")

# # execute git clone if not exists
# if not os.path.exists("ecdp-base"):
#     # branch feature/pontoon
#     os.system("git clone https://github.com/eCDP-translations/eCDP-Italian-pontoon.git ecdp-base")

# # Copy ecdp.nds to ecdp-base
# if not os.path.exists("ecdp-base" + os.path.sep + "ecdp.nds"):
#     shutil.copy("ecdp.nds", "ecdp-base")

# load the file "files_to_remove_keys.txt" in a list
with open("files_to_remove_keys.txt", "r") as f:
    files_to_remove = f.read().splitlines()

# Copy it folder to it_bak
shutil.copytree("it", "it_bak", dirs_exist_ok=True)

for root, dirs, files in os.walk("it"):
    for file in files:
        filepath = os.path.join(root, file)
        
        if file in files_to_remove and file.endswith(".json"):
            if is_json_dict(filepath):
                print(f"Removing keys from {filepath}")
                convert_dict_to_list(filepath)
            else:
                print(f"File {filepath} is not a dictionary")

# make dir if not exists ecdp-base\arm9\it
# make dir if not exists ecdp-base\bin\it
# make dir if not exists ecdp-base\overlay\it
# folders = ["arm9", "bin", "overlay"]
# for folder in folders:
#     if not os.path.exists("ecdp-base" + os.path.sep + folder + os.path.sep + "it"):
#         os.mkdir("ecdp-base" + os.path.sep + folder + os.path.sep + "it")

# for folder in folders:
#     shutil.copytree(
#         "it" + os.path.sep + "locales" + os.path.sep + "ja" + os.path.sep + folder + os.path.sep + "ja",
#         "ecdp-base" + os.path.sep + folder + os.path.sep + "it", dirs_exist_ok=True
#     )

# os.chdir("ecdp-base")

# # FIXME: copy cmcd/en.json to cmcd/it.json -> this is temp and should be removed
# shutil.copy("cmcd" + os.path.sep + "en.json", "cmcd" + os.path.sep + "it.json")

# # run ecdp-base\patch_all.py ecdp.nds -l it 
# os.system("python patch_all.py ecdp.nds -l it")

# ##########
# ### Clean
# ##########
# os.chdir("..")

# # remove it folder
# shutil.rmtree("it")

# # rename it_bak to it
# os.rename("it_bak", "it")

# os.chdir("scripts")
