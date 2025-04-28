import re

email = input("Enter your email: ")

if re.search(r".+@.+\.com",email):
    print("valid")
else:
    print("invalid email")