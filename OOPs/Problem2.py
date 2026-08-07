class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print(self.brand)

class Car(Vehicle):
    pass


v1=Vehicle("BMW")

v1.display()

c1=Car("AUDI")

c1.display()