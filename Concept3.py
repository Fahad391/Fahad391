class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0  # Private attribute

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            print(f"Accelerating. Current Speed: {self.__speed} Km/h")
        else:
            print("Amount to accelerate must be positive")
    
    def brake(self):
        self.__speed = 0
        print("Car stopped.")
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed can't be negative.")


my_car = Car("Toyota", "Camry")
my_car.accelerate(30)
print(my_car.get_speed())
my_car.set_speed(100)
print(my_car.get_speed())
