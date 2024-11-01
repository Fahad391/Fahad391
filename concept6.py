class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine starts with horsePower: ", self.horsepower)


class Car:
    def __init__(self, make, horsepower) :
        self.make = make
        self.engine = Engine(horsepower)
    
    def start_car(self):
        print(f"{self.make} car is starting")
        self.engine.start()

Rezvani = Car("Rezvani", 748)
Rezvani.start_car()
    