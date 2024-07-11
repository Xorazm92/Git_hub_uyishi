with open("IT.txt") as file:
    date = file.read()
    data = date.split("\n")[:-1]
    print(date)
    
    for i, val in enumerate(data):
        data[i] = val.split(" ")
        data[i][3] = int((data[i][3]))
            
    max_bonus = max(data, key=lambda x: x[3])[3]
    
    for it in data:
        ism, daraja, maosh, bonus, bolim = it
        if bonus == max_bonus:
            print("Eng yaxshi bo'lim: ", bolim)
        

