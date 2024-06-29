# python
import os
import json
import random

# for file in current dir recursive json
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".json"):
            # parse json if it is a dict or a list
            with open(os.path.join(root, file), "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        print("dict")
                    elif isinstance(data, list):
                        print("list")
                        # transform it in a dict with 6 random numbers as keys
                        data = { str(random.randint(0, 1000000)): x for x in data }
                        # overwrite the file
                        with open(os.path.join(root, file), "w") as f:
                            json.dump(data, f)
                except json.JSONDecodeError:
                    print("not json")

