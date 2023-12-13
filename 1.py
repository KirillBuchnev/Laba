def DigitCountSum(k,c):
    count = 0
    s = 0
    k = str(k)
    for i in k:
        if i == str(c):
            count +=1
            s += int(i)
    return count, s
try:
    k=int(input("Введите значение k: "))
    c1=int(input("Введите значение c1: "))
    c2=int(input("Введите значение c2: "))
    c3=int(input("Введите значение c3: "))
    c4=int(input("Введите значение c4: "))
    c5=int(input("Введите значение c5: "))
    if k<0:
        raise ValueError
    print("Значение функции при c1:",DigitCountSum(k,c1))
    print("Значение функции при c2:",DigitCountSum(k,c2))
    print("Значение функции при c3:",DigitCountSum(k,c3))
    print("Значение функции при c4:",DigitCountSum(k,c4))
    print("Значение функции при c5:",DigitCountSum(k,c5))
except:
    print("Данные некорректны")



