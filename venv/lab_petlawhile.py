##z= 0

#while z!=10:
    #print(z)
    #z+=1
#else:
    #print("Wyświetlonych zostało " + str(z) + " liczb")

#zad2

# lista= [4, 6, 2, 3, 5, 9, 1]
# print("Podaj liczbę, a sprawdzę czy różnica między wpisaną liczbą, a liczbą z listy jest równa 0")
# liczba = input("wpisz liczbę: ")
# licznik = 0
# while licznik < len(lista) - 1:
#     if int(liczba) - lista[licznik] == 0:
#         print(liczba + "-" + str(lista[licznik]) + " =0")
#         break
#     else:
#         licznik +=1


zad 3

lista = [4, 6, 2, 3, 5, 9, 1]
lista2 = [7, 3, 4, 6]
suma = []

for a in lista:
    for b in lista2:
        wynik = a+b
        suma.append(wynik)
    print(suma)
