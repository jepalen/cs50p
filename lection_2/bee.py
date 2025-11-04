WORDS = {"PAIR":4,"HAIR":4,"CHAIR":5, "GRAPHIC":7}

def main():
    print("Welcome to spelling bee!")

    for word,points in WORDS.items():
        print(f"{word} is {points} letters long.")  

    print("Too much help?")
    print("Your letters are:  A, I, P, C, R, H, G")
    while len(WORDS) > 0:
        print(f"there are {len(WORDS)} words left to guess.")
        guess = input("Enter a word: ").upper().strip()
        guess_try(guess)

    print("Congratulations! You won!")


def guess_try(guess):

    if guess in WORDS and len(guess) >=7:
        print(f"Correct! '{guess}' is {WORDS[guess]} letters long.")
        # del WORDS[guess] also works
        WORDS.clear()
        print("You found the longest word!")
  
    elif guess in WORDS:
        print(f"Correct! '{guess}' is {WORDS[guess]} letters long.")
        # del WORDS[guess] also works
        WORDS.pop(guess)
    else:
        print(f"Sorry, '{guess}' is not a valid word. Try again.")

main()        