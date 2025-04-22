name = input("What's your name? ")

match name:
    case "harry" | "hermoine" | "ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("whoo?")