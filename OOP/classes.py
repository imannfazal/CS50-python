class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name not entered!")
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return(f"{self.name} from {self.house} does {self.patronus}")
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell":
                return "🐶"
            case _:
                return "🥢"

def main():
    student = get_student()
    print(student.charm())

def get_student():
    # making object of Student class "student"
    name = input("Name: ")
    house = input("House: ")
    charm = input("Charm: ")
    return Student(name, house, charm)

if __name__ == "__main__":
    main()