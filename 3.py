def PowerN(x,n):
    if n==0:
        return 1
    if n>0 and n%2==0:
        return PowerN(x, n // 2)**2
    if n>0 and n%2!=0:
        return x * PowerN(x, n-1)
    if n<0:
        return 1 / PowerN(x, -n)
try:
    x=float(input("Введите значение x:"))
    n1=int(input("Введите значение N1:"))
    n2=int(input("Введите значение N2:"))
    n3=int(input("Введите значение N3:"))
    n4=int(input("Введите значение N4:"))
    n5=int(input("Введите значение N5:"))
    print("Значение функции при N1:",PowerN(x,n1))
    print("Значение функции при N2:",PowerN(x,n2))
    print("Значение функции при N3:",PowerN(x,n3))
    print("Значение функции при N4:",PowerN(x,n4))
    print("Значение функции при N5:",PowerN(x,n5))
except:
    print("Данные некорректны")
