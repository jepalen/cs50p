
''' 
Jeff P. 
2025-10
lection 0
calculator program
'''

def main():
    print("This is a simple calculator program.")
    x = float(input("Enter X number: "))
    y = float(input("Enter Y number: "))

    z = add(x, y)
    print("The rounded sum of X and Y is: ", z)
    print(f"{z:,}") #formatted with comma as thousands separator

    z = subtract(x, y)
    print("The difference of X minus Y is: ", z)

    z = multiply(x, y)
    print("The product of X and Y is: ", z)

    z = divide(x, y)
    print("The rounded division of X by Y is: ", z)
    print(f"{z:.2f}") #formatted to 2 decimal places

    z = expo(x, y)
    print("X to the power of Y is: ", z)



def add(x, y):
    z = round(x +  y )
    return z

def divide(x, y):
    z = round(x / y , 1)
    return z

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y 

def expo(x,y):
    return x ** y



main()