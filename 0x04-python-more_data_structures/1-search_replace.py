#!/usr/bin/python3
def square_matrix_simple (my_list, replace, search):
    return(list(map(lambda e: replace if e == search else e, my_list)))
