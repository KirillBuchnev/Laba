import random
def f(x):
    summa=0
    for i in x:
        summa+=i
    return summa
a1=[random.randint(-5,5) for i in range(20)]
a2=[random.randint(-5,5) for i in range(10)]
a3=[random.randint(-5,5) for i in range(15)]
try:
    x = float(input("Введите значение x:"))
    b = float(input("Введите значение b:"))
    c = float(input("Введите значение c:"))
    y1=f(a1)*x**2+b*x+c
    y2=f(a2)*x**2+b*x+c
    y3=f(a3)*x**2+b*x+c
    print("Значение функции:", y1,"При значениях a:",f(a1))
    print("Значение функции:", y2,"При значениях a:",f(a2))
    print("Значение функции:", y3,"При значениях a:",f(a3))   
except:
    print("Введено некорректные значения")
    