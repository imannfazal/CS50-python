class Student:
    def __init__(self, name, house):  
        self.name = name
        self.house = house
        # self.patronus = patronus
    def __str__(self):
        return(f"{self.name} from {self.house}")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name not entered!")
        self._name = name

    # getter
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ("Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"):
            raise ValueError("Invalid house!")
        self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🦌"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell":
    #             return "🐶"
    #         case _:
    #             return "🥢"

def main():
    student = get_student()
    print(student)

def get_student():
    # making object of Student class "student"
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()