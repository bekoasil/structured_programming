
class Vehicle:
    def __init__(self) -> None:
        print("A Vehicle Initialized")
    def go(self,distance):
        print("We traveled {}kms!".format(distance))

class Ship(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("A Ship is initialized")
    def sound(self):
        print("Woot Woot")

class Plane(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("A plane is initialized")
    def sound(self):
        print("Fiiiiuw")

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    def sound(self):
        print("Wroom Wroom")
    def go(self,distance):
        print("I would walk {} miles and I would walk {} miles more.".format(distance,distance))