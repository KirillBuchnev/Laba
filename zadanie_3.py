try:
    n = int(input("Введите количество стран: "))
    if n<=0:
        raise ValueError
    country_and_rivers = {}
    for i in range(n):
        country = input("Введите название страны: ") 
        rivers = []
        rivers_input = input("Введите названия рек через запятую: ")
        river = ""
        for bukva in rivers_input:
            if bukva != ",":
                river += bukva
            else:
                rivers.append(river)
                river = ""
        rivers.append(river)
        country_and_rivers[country] = rivers
    river_list = [] 
    river_input = input("Введите нужные вам реки через запятую: ")
    river = ""
    for bukva in river_input:
        if bukva != ",":
            river += bukva
        else:
            river_list.append(river)
            river = ""
    river_list.append(river)
    for river in river_list:
        river_found = False
        for country, rivers in country_and_rivers.items():
            if river in rivers:
                print(f"Река {river} протекает в стране {country}")
                river_found = True
        if not river_found:
            print(f"Река {river} отсутствует в словаре стран и рек")
except:
    print("Введенно некорректное значение")

