import sys

if len(sys.argv) < 2:
    print("not enough arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("My name is",sys.argv[1])