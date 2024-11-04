#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe


lista = list(range (10))
print(lista)
print(len(lista))

for pos in range(len(lista)):
    print(pos)
    lista[pos] += lista[pos-1]

print (lista)
    