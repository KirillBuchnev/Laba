import random
try:
    def poisk_pervachkov_v_DSTU (spisok):
        spisok_2 = []
        for i in range(len(spisok)):
            for j in range(len(spisok[i])):
             if spisok[i][j] not in spisok_2:
                spisok_2.append(spisok[i][j])
        return spisok_2
    m = int(input("Введите значения M:"))
    n = int(input("Введите значения N:"))
    if n<=0 or m<=0:
        raise ValueError
    spisok = []
    for i in range(m):
        spisok.append([random.randint(0,10) for j in range(n)])
    for i in range(m):
            print(spisok[i])
    print("Неповторяющиеся элементы" , poisk_pervachkov_v_DSTU(spisok))  
except:
    print("Введены неверные параметры для двумерного списка")

