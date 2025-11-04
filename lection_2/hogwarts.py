def exercise1():
    students = ["Hermione", "Harry", "Ron", "Draco", "Neville"]

    for student in students:
        print(f"Welcome to Hogwarts, {student}!")

    for i in range(len(students)):
        print(f"goodbye {i+1} {students[i]}!")   

def exercise2(): 
    students=[
        {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
        {"name": "Neville", "house": "Gryffindor", "patronus": "unicorn"}
    ]

    for student in students:
        name = student["name"]
        house = student["house"]
        patronus = student["patronus"] if student["patronus"] else "no patronus" 
        print(f"{name} has been assigned to {house} house and their patronus is {patronus}.")

def main():
    exercise1()
    exercise2()

main()