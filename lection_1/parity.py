def main():
    x = int(input("Enter X: "))
    if is_even(x):
        print(f"{x} is even")
    else:
         print(f"{x} is odd")


    print("Using second function:") 
    if is_odd(x):
        print(f"{x} is odd")
    else:
         print(f"{x} is even")


def is_even(n):
    return True if n % 2 == 0 else False

def is_odd(n):
    return n %2 != 0

main()    