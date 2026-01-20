class Vehicle:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def move(self):
        print("move!")

class Car(Vehicle):
    pass

class Ship(Vehicle):
    def move(self):
        print("sail!")

p1 = Car("Ford", "Mustang")
p2 = Ship("Ibiza", "Lolo")

for x in (p1, p2):
    print(x.name, x.model)
    x.move()