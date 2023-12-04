try:
    n = int(input("Введите значения N:"))
    if n<=0:
        raise ValueError
    country_and_rivers = {}
    for i in range(n):
        country, river = input("Введите название страны и реки через пробел: ").split()
        country_and_rivers[river] = country
    rivers = input("Введите список названий рек, разделенных пробелом: ").split()
    for river in rivers:
        if river in country_and_rivers:
            print(f"Река {river} протекает в стране {country_and_rivers[river]}")
        else:
            print(f"Река {river} отсутствует в словаре стран и рек")
except:
    print("Введенно некорректное значение")



























































# try:
#     n = int(input("Введите значения N (не более 5):"))
#     if n<=0 or n>5:
#         raise ValueError
#     country_and_rivers = {}
#     country, river = ("Россия Дон").split()
#     country_and_rivers[river] = country
#     rivers = ("Дон").split()
#     for river in rivers:
#         if river in country_and_rivers:
#             print(f"Река {river} протекает в стране {country_and_rivers[river]}")
#         else:
#             print(f"Река {river} отсутствует в словаре стран и рек")
# except:
#     print("Введенно некорректное значение")