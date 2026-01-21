# file = open("demofile.txt", "rt")
# print(file.read())

with open("demofile.txt", "rt") as f:
    for x in f:
        print(x)

import os

if os.path.exists("students.csv"):
    os.remove("students.csv")