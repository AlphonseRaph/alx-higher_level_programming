#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = abs(number) % 10
if number < 0:
    no = -no
if no > 5:
    print(("Last digit of {:d} is {:d} and is greater than 5"
           .format(number, no)))
elif no == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, no))
elif no < 6 and no != 0:
    print(("Last digit of {:d} is {:d} and is less than 6 and not 0"
           .format(number, no)))
