def is_griffindor(student):
    return student["house"] == "Gryffindor"

def add_to_griffindor(students):
    griffindor = [{"name": student,"house":"Gryffindor"} for student in students]
    print('list students',griffindor)
    griffindor ={student: "Gryffindor" for student in students}
    print('dict students',griffindor)

def enumerate_students(students):
    for i, student in enumerate(students):
        print(i+1, student)
## using set to remove duplicates
students = [
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
]

# three posibilities to get the griffindor student's names
griffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
for griffindor in sorted(griffindor):
    print("pythonic", griffindor)

griffindor = filter(lambda student: student["house"] == "Gryffindor", students)
for griffindor in sorted(griffindor, key=lambda student: student["name"]):
    print("lambda", griffindor["name"])


griffindor = filter(is_griffindor, students)
for griffindor in sorted(griffindor, key=lambda student: student["name"]):
    print("functional", griffindor["name"])


houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

students = ["Hermione Granger", "Harry Potter", "Ron Weasley", "Draco Malfoy"]  

add_to_griffindor(students)

enumerate_students(students)
