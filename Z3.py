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
        xs.append(float(input(f"Введите {i} элемент списка:")))
    return xs
def new_list(list):
    new_list = []
    for i in list:
        if i%1 != 0:
            new_list.append(round(i%1,2))
    return new_list    
n = InputNumber()    
list = createlist(n)
new_list = new_list(list)
print(f"разницу между максимальным и минимальным значением дробной части элементов {round(max(new_list) - min(new_list),2)}")