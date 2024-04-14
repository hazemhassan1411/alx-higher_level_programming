#!/usr/bin/python3
def square_matrix_simple (my_list, replace, search):
    return list(map(lambda g: replace if g == search else g, my_list))
