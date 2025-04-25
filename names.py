file = open("Names.txt", "r")
for name in file:
    print(name, end="")

file.close()
