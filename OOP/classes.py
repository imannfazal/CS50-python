class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name not entered!")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is in {student.house}")

def get_student():
    # making object of Student class "student"
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()