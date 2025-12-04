class Wizard(Student):
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Hermione Granger", "Gryffindor")
professor = Professor("Severus Snape", "Dark Arts")
print(student.name)
print(professor.name)
