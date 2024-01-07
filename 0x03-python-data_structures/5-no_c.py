#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in range (len(my_string)):
        if i == 'c' or i == 'C':
            continue
        else:
            new_string = new_string + my_string[i]
    return new_string
