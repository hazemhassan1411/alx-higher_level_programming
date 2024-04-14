#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for r in sorted(a_dictionary.keys()):
        print("{}: {}".format(r, a_dictionary[r]))
