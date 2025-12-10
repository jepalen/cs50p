## using mipy and global variable inside a class
#if a function does not return anything returns None
class Cat:
    MEOWS = 3

    def meow(self)->None:
        '''
        meow function 
        
        :param n: number of times to meow
        :type n: int
        :raises ValueError: if n is negative
        :return: None
        ''' 
        for _ in range(Cat.MEOWS):
            print("meow")

    def sleep(self,hours:int)->None:
        '''sleep function '''
        for _ in range(hours):
            print("Zzz")


def main():
    cat = Cat()
    cat.meow()
    hours:int = int(input("Hours: "))
    cat.sleep(hours) 
    mistake = cat.sleep(hours) 
    assert mistake is None 

if __name__ == "__main__":
    main()
