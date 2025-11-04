def inputVal ():
    while True:
        n= int(input('Give a positive value for n: '))
        if n>0:
            #here we can also use break and return the value after the loop
            return n
        else:
            continue
    

def main():
    i =3 
    while i != 0:
        print('meow')
        i= i-1
    #2nd way
    i = 0
    while i < 3:
        print('meow 2.0')
        i+=1

    # a loop in a list but if the list is too long we can have problems writing all values  in the list
    i=0
    for i in [0,1,2]:  
        print('meow inside for')

    #good approach
    i=0
    for i in range(3):
        print('meow inside for 2.0')

    #best approach in pythonic way
    i=0
    for _ in range(3):
        print('meow inside for 3.0 without a variable')

    #even more pythonic way
    print('meow wow\n'*3,end='')

    n= inputVal()
    i=0
    for _ in range(n):
        print('meow n times')


main()