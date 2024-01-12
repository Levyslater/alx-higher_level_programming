#!/usr/bin/python3
""" script that adds all arguments to a Python list,
 and then save them to a file
"""

import json

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

with open('add_item.json', "a", encoding="utf-8") as f:
    filename = "add_item.json"
    for i in range(1, len(argv)):
        save_to_json_file(argv[i], filename)
