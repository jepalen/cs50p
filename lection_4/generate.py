import random

# from random import choice

coin = random.choice(["Heads", "Tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack", "Queen", "king"]
random.shuffle(cards)
print(cards)
print(random.choice(cards))
print(
    random.choices(cards, weights=[100, 0, 0], k=2)
)  # the options out can be repeated and with weight 100  the first element always appear
print(random.sample(cards, k=2))  # same as choices but without repeating element

random.seed(1)
print(random.choices(cards, k=2))

random.shuffle(cards)
print(cards)
