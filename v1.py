n = int(input("Nechtalik ro'yxat kiritasiz: "))
lst1 = []

for i in range(n):
    lst1.append(int(input(f"{i+1}-chi elementni kiriting: ")))

lst2 = []

for i in range(len(lst1)-1):
    if lst1[i] * lst1[i+1] > 0: 
        lst2.append(f"{lst1[i]} {lst1[i+1]}")
     

print("lst2 ro'yxati:", lst2)
