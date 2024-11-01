class Car:
    def __init__(self):
        self.started = False
        self.driving = False
    
    def start(self):
        if not self.started:
            self.started = True
            print("Car started")
        else:
            print("Car is already started")
    
    def drive(self):
        if not self.driving:
            self.driving = True
            print("Car is driving")
        else:
            print("Car is already driving")
    
    def command(self):
        while True:
            user = input("Command: ")
            if user.upper() == 'Start':
                vehicle.start()
            if user.upper() == 'Drive':
                vehicle.drive()
            if user.upper() == 'Stop':
                print("Stopping")
                print("Car stopped")
                break
            elif user.upper() == 'Go to':
                if not self.started:
                        print("Start the car first")
                elif not self.driving:
                    print("Start the drive mode first")
                else:
                    destination = input("Location: ")
                    print(f"Car is driving to {destination}")



vehicle = Car()
vehicle.command()
