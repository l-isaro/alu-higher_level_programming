#!/usr/bin/python3
for i in range(101):
    if i == 100:
        print()
    else:
        print("0{:02d}, ".format(i), sep=", ",end='')
        
