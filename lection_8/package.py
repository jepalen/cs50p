class Package:
    def __init__(self, number, sender,recipient,weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.number} from {self.sender} to {self.recipient} with weight {self.weight}kg"

    def calculate_cost(self,price_per_kg):
        return self.weight * price_per_kg

def main():
    packages=[
    Package(number=1,sender="John", recipient="Jane", weight=1),
    Package(number=2,sender="Jeny", recipient="Doe", weight=20)
    ]

    for package in packages:
        print(f"{package} costs {package.calculate_cost(10)}€")    

if __name__ == "__main__":
    main()
