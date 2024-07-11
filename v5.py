def naqsh(colors):
    time = 0
    bor_rang = None
    for color in colors:
        if color != bor_rang:
            time += 1  
        time += 2  
        bor_rang = color
    return time

colors = []

while True:
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Green")
    print("5. Blue")
    print("6. Brown")
    print("7. Black")
    print("8. White")
    print("0. Chiqish va natijani ko'rish")
    select = int(input("Tanlang >>> "))

    if select == 0:
        print("Chiqmoqda...")
        break
    elif select == 1:
        colors.append("Red")  
    elif select == 2:
        colors.append("Orange")  
    elif select == 3:
        colors.append("Yellow")  
    elif select == 4:
        colors.append("Green")  
    elif select == 5:
        colors.append("Blue")  
    elif select == 6:
        colors.append("Brown")  
    elif select == 7:
        colors.append("Black")  
    elif select == 8:
        colors.append("White")  
    else:
        print("Noto'g'ri kirish, qayta kiriting")
        continue

    print("Hozirgi ranglar:", colors)

time = naqsh(colors)
print("Umumiy natija:", time)
