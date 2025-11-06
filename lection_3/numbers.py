def main():
    x= get_int('put a number X: ')
    print(f'the number X is: {x}')

# def get_int ():
#     while True:
#         try:
#             number = int(input('put a number X: '))
#         except ValueError:
#             print(f' X is not an integer')
#         else:
#             break
#     return number

def get_int (promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass



main()