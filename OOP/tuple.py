def main():
    student = get_student()
    # we can not change the value of house just like we are doing below bcs in the function we returned a tuple not a list
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} is from {student[1]}")

def get_student():
    name =  input("whats the name? ")
    house = input("whats the house? ")
    # making tuple.
    # its value can not be changed unlike lists.
    # () => tuple while [] => lists
    return (name, house)

if __name__ == "__main__":
    main()