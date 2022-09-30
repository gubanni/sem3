import random
def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите длину списка: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def createlist(n):
    xs = []
    for i in range(n):
        xs.append(random.randint(0,20))
    return xs

def new_list(list):
    
    if len(list) % 2 == 0:
        new_len = len(list)//2
    else:
        new_len = len(list)//2 + 1 
    new_list = []
    for i in range(new_len):
        new_list.append(list[i]*list[len(list)-i-1])
    return new_list    
n = InputNumber()    
list = createlist(n)


print(f"{list} -> новый список: {new_list(list)}")