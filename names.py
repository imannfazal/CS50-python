with open("Names.txt", "r") as file:
    names = file.readlines()

for name in sorted(names):
    if len(name)<=7:
        print(name, end="")


