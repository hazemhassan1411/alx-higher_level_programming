#!/usr/bin/python3
def search_replace (my_list, replace, search):
    return list(map(lambda e: replace if e == search else e, my_list))
