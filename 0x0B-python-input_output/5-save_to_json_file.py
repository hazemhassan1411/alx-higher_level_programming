#!/usr/bin/python3
"""hazem is here"""

import json


def save_to_json_file(my_obj, filename):
    """hazem is here"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
