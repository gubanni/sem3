import random

def createlist():
    xs = []
    for i in range(10):
        xs.append(random.randint(0,20))
    return xs

def summ(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]       
    return sum
list = createlist()

print(f"{list} -> сумма элементов на нечётных позициях: {summ(list)}")