#!/usr/bin/python3
"""hazem is here"""

import json


def load_from_json_file(filename):
    """hazem is here"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f)
