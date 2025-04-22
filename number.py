def main():
    int = get_int("What's x? ")
    print(f"x is {int}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            # print("number is not integer")
            pass

main()