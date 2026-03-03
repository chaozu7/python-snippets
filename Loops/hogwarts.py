students = ["Harry", "Hermione", "Ron", "Draco"]
houses = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}


# for student in students:
#    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

for house in houses:
    print(house, houses[house])
