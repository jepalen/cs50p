import random

class Hat:
    houses=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] 

    @classmethod
    def sort(cls,student):
        return random.choice(cls.houses)

print(Hat.sort(input("Name: ").strip()))