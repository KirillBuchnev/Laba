import random
def f(x):
    summa=0
    for i in x:
        summa+=i
    return summa
a=[random.randint(-5,5) for i in range(20)]
b=[random.randint(-5,5) for i in range(10)]
c=[random.randint(-5,5) for i in range(15)]
try:
    x = float(input("Введите значение x: "))
    y=f(a)*x**2+f(b)*x+f(c)
    print("Значение функции:", y,"При значениях a,b,c(",f(a),f(b),f(c),")")   
except:
    print("Введено некоректное значение x")
    