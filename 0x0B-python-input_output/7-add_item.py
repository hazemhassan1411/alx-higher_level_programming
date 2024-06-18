#!/usr/bin/python3
"""hazem is here"""

import sys
import os

# Import the functions from the previous tasks
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Initialize the list
try:
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        items = load_from_json_file(filename)
    else:
        items = []
except Exception:
    items = []

# Add all arguments to the list
items.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(items, filename)