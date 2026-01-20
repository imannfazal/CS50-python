class Add:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True
    
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

p1 = Add()
p1.add(4)
p1.add(7)
print(p1.result)