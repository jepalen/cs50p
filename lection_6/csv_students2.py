import csv
students = []

name= input('Name: ')
country= input('Country: ')

with open('students2.csv','a') as file:
    writer = csv.DictWriter(file,['name','country'])
    writer.writerow({"name":name,"country":country})

with open('students2.csv') as file:
    reader= csv.DictReader(file)
    for row in reader:
        students.append(row)
        #students.append({"name":row['name'],"country":row['country']})

for student in sorted(students,key=lambda student:student['country'],reverse=False):
     print(f"{student['name']} is in {student['country']}")  