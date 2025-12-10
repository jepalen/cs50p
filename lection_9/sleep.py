def main():
    n = int(input("Number: "))
    
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield 'sheep' *i

if __name__ == "__main__":
    main()