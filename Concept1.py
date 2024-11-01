class Drone:
    def __init__(instance, brand, model ):
        instance.brand = brand
        instance.model = model   
        instance.turned_on = False
    def display(instance):
        print(f"{instance.brand} Model: {instance.model}")
    
    def turn_on(instance):
        if not instance.turned_on:
            instance.turned_on = True
            print("Drone is turned On")
        else:
            print("Drone is already turned On")
    
    def turn_off(instance):
            print("Drone is turned off")
    
    def command(instance):
        while True:
            user = input("Command: ")
            if user.capitalize() == 'Turn on':
                drone.turn_on()
            elif user.capitalize() == 'Turn off':
                drone.turn_off()
                break

drone = Drone("DJI", "DJI Mavic 3 Pro")
drone.display()
drone.command()
