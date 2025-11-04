def main():
    print_column(3)
    print_square(4)
    print_square2(5)


def print_column(n):
    for _ in range(n):
        print("#")

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def print_square2(size):
    for i in range(size):
        print("#" * size)

main()