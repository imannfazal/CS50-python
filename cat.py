def main():
    number = getnumber()
    meow(number)

def getnumber():
    while True:
        n = int(input("enter number: "))
        if n>0:
            return n
        else:
            continue

def meow(n):
    print("meow\n"*n , end="")

if __name__ == "__main__":
    main()