#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')

print("{} => {}".format("a", "lower" if islower("a") else "upper"))
print("{} => {}".format("H", "lower" if islower("H") else "upper"))
print("{} => {}".format("A", "lower" if islower("A") else "upper"))
print("{} => {}".format("3", "lower" if islower("3") else "upper"))
print("{} => {}".format("g", "lower" if islower("g") else "upper"))
