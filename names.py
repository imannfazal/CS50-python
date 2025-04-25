file = open("Names.txt", "r")
for name in file:
    if len(name)==7:
        print(name, end="")

file.close()
