try:
    def summa(spisok):
        totals = []
        for chisla in spisok:
            total = 0
            for x in chisla:
                total += x
            totals.append(total)
        return totals
    m = int(input("Введите значение M: "))
    n = int(input("Введите значение N: "))
    if n <= 0 or m <= 0:
        raise ValueError
    spisok = []
    for i in range(m):
        spisok.append([(i + 1) + (j + 1) for j in range(n)])
    for i in range(m):
        print(spisok[i])
    print("cумма каждой из строк (через запятую)",summa(spisok))
except:
    print("Введены неверные параметры для двумерного списка")
# try:
#     m = int(input("Введите значение M: "))
#     n = int(input("Введите значение N: "))
#     if n <= 0 or m <= 0:
#         raise ValueError
#     mat = []
#     for i in range(m):
#         stroka = []
#         for j in range(n):
#             zapolnenie = ((i+1)+(j+1))
#             stroka.append(zapolnenie)
#         mat.append(stroka)
#     for stroka in mat:
#         print(stroka)
#     for i in range(m):
#         stroka_sum = 0
#         for j in range(n):
#             stroka_sum += mat[i][j]
#         print("Сумма элементов строки номер", i + 1, "-", stroka_sum)
# except:
#     print("Введены неверные параметры для двумерного списка")