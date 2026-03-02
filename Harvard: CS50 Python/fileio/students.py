students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
     #1   print(f"{name} is in {house}")
     #2   students.append(f"{name} is in {house}")
        
#2 for student in sorted(students):
#2    print(student)

# version with a dictionary

        student = {}
        student = {"name": name, "house": house}
     #  student["name"] = name
     #  student["house"] = house
        students.append(student)
        
#def get_house(student):
#    return student["house"]

#def get_name(student):
#    return student["name"]
        
#for student in sorted(students, key=get_house, reverse=True):
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")