names = []
name = input('what is your name: ')


#file = open('names.txt','a') # 'w' write and dont append
#file.write(f'{name}\n')
#file.close()

# the pythonic way for open a file for write and not need to call .close
with open('names.txt','a') as file:
    file.write(f'{name}\n')

#with open('names.txt','r') as file:
#    lines = file.readlines()

#for line in lines:
#    print(f'Hello: {line}') 

# the pythonic way for reading a file and not need to call .close
# with open('names.txt','r') as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print('Hello:', name) 

# more pythonic way
with open('names.txt','r') as file:
    for line in sorted(file,reverse=True, key=None):
        print('Hello:',line.rstrip())   