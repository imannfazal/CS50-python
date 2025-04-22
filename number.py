while True:
    try:
        number = int(input("enter x: "))
    except:
        print("number is not integer")
    else:
        break

print(f"x is {number}")