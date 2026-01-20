class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if(age>0):
            self.__age = age
        else:
            print("Age must be Positive!")

p1 = Person("iman", 25)
name = p1.name
age = p1.get_age()
print(f"{name} is {age}")

p1.set_age(23)
print(f"{name} is {p1.get_age()}")