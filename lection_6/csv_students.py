import csv
students = []

def get_country(student):
    return student['country']

with open('students.csv') as file:
    reader= csv.reader(file)
    for name, country in reader:
        students.append({"name":name,"country":country})


for student in sorted(students,key=lambda student:student['country'],reverse=False):
     print(f"1st: {student['name']} is in {student['country']}")  

