# the quantity of elements in the list or dictionary  should be the same as the arguments of the function
def total(galeons, sickles, knuts):
    return (galeons * 17 +sickles) * 29 + knuts

def f(*args,**kwargs):
    print('positional arguments',args)
    print('keyword arguments',kwargs)

def main():
    coins = [100, 50, 25]

    print(total(*coins))

    coins = {"galeons": 10, "sickles": 5, "knuts": 2}

    print(total(**coins))

    f(1,2,3,4,5,6,7,8,9,10, name="John", age=30)

if __name__ == "__main__":
    main()