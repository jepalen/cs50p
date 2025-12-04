class Student:
    def __init__(self, name, house,patronus=None):
        # goes to the property setter name ,not use here self._name
        self.name = name
        # goes to the property setter house ,not use here self._house
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse"
            case "Otter":
                return "Bug"
            case "Jack Russell Terrier":
                return "dog"
            case _:
                return "ghost"

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        house = input("House: ").strip()
        patronus = input("Patronus: ").strip()
        return Student(name, house,patronus)

def main():
    student = Student.get()
    print(student)
    print('Expecto Patronum!')
    print(student.charm())


# # tuples don't allow to modify the values
# def get_student_via_tuple():
#     name = input("Name: ").strip()
#     house = input("House: ").strip()
#     return (name, house)

# # lists allow to modify the values
# def get_student_via_list():
#     name = input("Name: ").strip()
#     house = input("House: ").strip()
#     return [name, house]

# def get_student_via_dict():
#     name = input("Name: ").strip()
#     house = input("House: ").strip()
#     return {"name": name, "house": house}


if __name__ == "__main__":
    main()
