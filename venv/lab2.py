lista= ["wyraz", 3, 5.7, 32, [4, 6, 5]]
print(lista)

lista.append(5)
lista.append('12')
print(lista)

lista.insert(2, 4.76)
lista.insert(10, 14)
print(lista)

lista.pop(2)
print(lista)

lista.remove(32)
print(lista)

del lista[5]
print(lista)

lista.extend((2, 2, 'n'))
print(lista)

lista.reverse()
print(lista)

nowa_lista = [4, 1.2, 5, 7, 2, 3, 1.78]
nowa_lista.sort()
print(nowa_lista)

