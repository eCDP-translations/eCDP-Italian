#!/usr/bin/env python3

from pathlib import Path
import json

# scan subdirs from current directory
for jsonfile in Path(".").glob("**/*.json"):
    try:
        json.load(open(jsonfile))
        pass
    except Exception as e:
        print(jsonfile, "fail", e)
