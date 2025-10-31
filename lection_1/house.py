name = input("whats your name? ")

if not (name == "" or name.isspace()):
    print("hello ", name)
else:
    print("you didn't enter a name")    

match name:
    case "Harry" | "Hermione" | "Ron":  
        print("griffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("who are you?")