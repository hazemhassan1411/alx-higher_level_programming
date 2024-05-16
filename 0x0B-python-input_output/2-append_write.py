#!/usr/bin/python3
"""hazem is here"""


def append_write(filename="", text=""):
    """hazem is here"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
