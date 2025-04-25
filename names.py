names = []

for _ in range(4):
    names.append(input("What's your name? "))

print(names)

for name in sorted(names):
    print("Hello, "+ name)