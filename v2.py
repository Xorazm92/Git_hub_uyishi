a = int(input("Nechta dict ma'lumot kiritasiz: "))
dct = {}

for i in range(a):
    key = input(f"{i+1}-chi kalit so'zni kiriting: ")
    value = int(input(f"{i+1}-chi 0 yoki 1 kiriting: "))
    dct[key] = value
    
count = {1: [], 0: []}
for name, vote in dct.items():
    count[vote].append(name)

if len(count[1]) == len(count[0]):
    natija = [0] + sorted(count[0] + count[1])
elif len(count[1]) > len(count[0]):
    natija = [1] + sorted(count[1])
else:
    natija = [0] + sorted(count[0])

print("Natija:", natija)


    

