with open("Names.csv") as file:
    for line in sorted(file, reverse=True):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


