students = []

def get_country(student):
    return student['country']

# more pythonic way
with open('students.csv','r') as file:
    for line in sorted(file,reverse=True, key=None):
        row = line.rstrip().split(',')
        name, country = line.rstrip().split(',')
        students.append({"name":name,"country":country})
        print(f'Hello: {row[0]} is in {row[1]}')   
        print(f'Another: {name} is in {country}') 

# for student in sorted(students,key=get_country,reverse=False):
#     print(f"3rd: {student['name']} is in {student['country']}")  

#pythonic way  using lambda for calling functions anonimous (without. a name)
for student in sorted(students,key=lambda student:student['country'],reverse=False):
     print(f"3rd: {student['name']} is in {student['country']}")  