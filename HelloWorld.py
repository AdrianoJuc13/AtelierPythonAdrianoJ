
listuta =[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Inainte de sortare", listuta)
print("Sortata ascendent", sorted(listuta))
print("Dupa sortare", listuta)
listuta2 = listuta[:]
listuta2.sort(reverse=True)
print("Sortata descendent",listuta2)
print("Dupa sortare", listuta)
print("Numerele pare ", listuta2[0::2])
print("Numerele impare ", listuta2[1::2])
print("Multiplii lui 3 sunt: ",end="")
for i in range(0, len(listuta)):
    if i % 3 == 0:
        print(f"{i}", end=", ")
