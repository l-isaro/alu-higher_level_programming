#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        highest = my_list[0]
        for i in range(len(my_list)):
                if highest < my_list[i]:
                    highest = my_list[i]
        return highest
    else:
        return None
