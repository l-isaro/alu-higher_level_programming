#!/usr/bin/python3
def uppercase(str):
    string = []
    for i in str:
        if i.isalpha() and 96 < ord(i) < 123:
            string.append(chr(ord(i) - 32))
        else:
            string.append(i)
    print("".join(string))
