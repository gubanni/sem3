def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите число: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def ConvertNumber(n):
    m = n
    st = ""
    while m != 0:
        st = str(m%2) + st
        m = m//2
    return st

number = InputNumber()
convertnumber = ConvertNumber(number)

print(convertnumber)