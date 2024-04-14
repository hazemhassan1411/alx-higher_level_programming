#!/usr/bin/python3
def search_replace (my_list, replace, search):
    return list(map(lambda g: replace if g == search else g, my_list))
