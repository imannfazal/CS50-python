while True:
    try:
        x= int(input("Enter x: "))
    except ValueError:
        print("x is not integer")
    else: 
        break
        
while True:
    try:
        y=int(input("Enter y: "))
    except ValueError:
        print("y is not integer")
    else:
        break
print(x+y)