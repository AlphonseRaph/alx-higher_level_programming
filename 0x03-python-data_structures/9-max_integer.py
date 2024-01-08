#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = my_list[0]
        for i in range(len(my_list) - 1):
            if my_list[i+1] > x:
                x = my_list[i+1]
        return x
    else:
        return None
