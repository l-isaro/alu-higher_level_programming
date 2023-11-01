#!/usr/bin/python3
for i in range(10):
    for n in range(10):
        if i == 8 and n == 9:
            print("{}{}".format(i, n))
        elif i < n:
            print("{}{}, ".format(i, n), end='')
