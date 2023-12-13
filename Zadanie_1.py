import random
try:
    m = int(input("Введите значения M:"))
    n = int(input("Введите значения N:"))
    if n<=0 or m<=0:
        raise ValueError
    spisok = []
    slovar = {}
    for i in range(m):
        stroka = []
        for j in range(n):
            chisla = random.randint(0,10)
            if chisla in slovar:
                slovar[chisla] += 1
            else:
                slovar[chisla] = 1
            stroka.append(chisla)
        spisok.append(stroka)
    for i in range(m):
            print(spisok[i])
    otvet= []
    for zhach, kolich in slovar.items():
         if kolich == 1:
              otvet.append(zhach)
    print("Неповторяющиеся элементы" , otvet)
except:
    print("Введены неверные параметры для двумерного списка")

