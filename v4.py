def raqam(n):
    x=sum(int(son) for son in str(n))
    return x

def sortla(lst):
    lst.sort(key=raqam)
    return lst
lst =[]

a =int(input("listga nechta ma'lumot kiritasiz: "))
for i in range(a):
    malumot = int(input(f"{i+1} -chi malumotni kiriting: "))
    lst.append(malumot)

# lst = [14, 30, 103]
print('Sortli royxat:', sortla(lst))