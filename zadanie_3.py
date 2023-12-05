try:
    n = int(input("Введите количество стран:"))
    if n<=0:
        raise ValueError
    country_and_rivers = {}
    for i in range(n):
        country = input("Введите название страны:")
        rivers = input("Введите список названий рек, разделенных пробелом: ").split()
        country_and_rivers[country] = rivers
    river = input("Введите список  нужных вам названий рек, разделенных запятой: ").split(",")
    for i in river:
      for country, rivers in country_and_rivers.items():
        if i in rivers:
            print(f"Река {i} протекает в стране {country}")
        else:
            print(f"Река {i} отсутствует в словаре стран и рек")
except:
    print("Введенно некорректное значение")