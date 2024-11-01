class Species:
    is_alive = True

class Animal(Species):
    def __init__(living, identify_animal):
        living.identify_animal = identify_animal
    
    def eat(living, meal):
        living.meal = meal
        print(f"{living.identify_animal} is eating {living.meal}")
    
    def fight(living):
        print(f"{living.identify_animal} is fighting")
    def sleep(living):
        print(f"{living.identify_animal} is sleeping")


class Plant(Species):
    def __init__(living, identify_plant, bear):
        living.identify_plant = identify_plant
        living.bear = bear
    def observe(living):
        print(f"This plant is a {living.identify_plant}")
        print(f"It bears {living.bear}")

class Hunting_animal(Animal):
    def hunt(living, prey):
        living.prey = prey
        print(f"the {living.identify_animal} is hunting a {living.prey}")
    def search_prey(living):
        print(f"{living.identify_animal} is looking for prey to hunt")

class Vegeterian_animal(Animal):
    def search_food(living):
        print(f"{living.identify_animal} is looking for food to eat")


Animal_1 = Hunting_animal("Tiger")
Animal_1.fight()
Animal_1.hunt('Horse')
Animal_1.eat('the horse')
Animal_2 = Vegeterian_animal("American Byson")
Animal_2.search_food()
Animal_2.eat("Plant leaf in the Farm")
plant_1 = Plant('Mango tree', 'Mangos')
plant_1.observe()
