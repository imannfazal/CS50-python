def main():
    int = get_int()
    print(f"x is {int}")

def get_int():
    while True:
        try:
            return int(input("enter x: "))
        except:
            # print("number is not integer")
            pass

main()