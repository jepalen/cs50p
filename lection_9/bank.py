# using global variables
balance = 0

def main():
    print("Balance:", balance)
    withdraw(10)
    deposit(1)
    print("Balance:", balance)

def withdraw(n):
    global balance
    balance -= n

def deposit(n):
    global balance
    balance += n

if __name__ == "__main__":
    main()
    