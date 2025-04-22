def main():
    print_brick(4)

def print_brick(bricks):
    for i in range(bricks):
        for j in range(bricks):
            print("#", end="")
        print()

main()