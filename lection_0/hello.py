
''' 
Jeff P. 
2025-10
lection 0
hello world program
'''

# Basic Documentation : docs.python.org/3/library/index.html

def hello(name="world 2"):
    print("Welcome to this \"new\" course", end=' ;) \n') #rewrite end parameter to avoid newline
    #remove leading/trailing whitespace, capitalize first letter of each word,
    name=name.strip().capitalize().title() 

    #split into first and last name
    first, last = name.split(" ")
    print("hello world, " + "it's me", first )
    print(f"{last} is a nice lastname" ) #f-string version


def main():
    # Ask the user for their name
    name = input("what's your full name? ")
    hello()
    hello(name)


main()