class Food:
    base_hearts=1
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(self.ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts=cls.base_hearts
        for ingredient in ingredients:
            if ingredient == "tomato":
                hearts +=2
            else:
                hearts+=1
        return hearts

    @classmethod
    def from_nothing(cls,hearts):
        food =cls(ingredients=[])
        food.hearts=hearts
        return food

def main():
    food = Food(["tomato", "cheese", "meat"])
    print(f"{food.ingredients} have {food.hearts} hearts")

    food2 = Food.from_nothing(5)
    print(f"{food2.ingredients} have {food2.hearts} hearts")

if __name__ == "__main__":
    main()