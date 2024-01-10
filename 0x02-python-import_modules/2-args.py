#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) >= 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{:d}: {}".format(i, arg))
