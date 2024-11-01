class Institute:
    name = "Abhijeet Dalla Academy"
    number_of_students = 0

    def __init__(self, name, standard):
        self.name = name
        self.standard = standard
        Institute.number_of_students += 1

print(Institute.name)
student_1 = Institute('Abdul Rahim Telgi', '5th Standard')
student_2 = Institute('Neeraj Agarwal', '9th Standard')
student_3 = Institute('Nalla Sivam', '3rd Standard')
print(f"Number of students: {Institute.number_of_students}")        
