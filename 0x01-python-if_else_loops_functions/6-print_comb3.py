#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i + 1, 10):
        print("{:02d}, {:02d}".format(i - 1, j), end=", " if i < 9 else "\n")
