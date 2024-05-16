#!/usr/bin/python3
"""hazem is here"""


def write_file(filename="", text=""):
    """hazem is here"""
    with open(filename, "w", encoding='utf-8') as file:
        print(file.write(text))
