#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe


lista = list(range (10))
print(lista)
print(len(lista))

for item in lista:
    pos = lista.index(item) 
    print (f"{pos} : {item}", end= " -> " )
    lista[pos] = item + lista [pos-1]
    print (f"{pos} : {item}" )