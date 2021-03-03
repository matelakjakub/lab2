from math import *
import sys as system

system

#zad1
# listasportow=["piłka nożna", "podnoszenie ciężarów", "piłka ręczna", "siatkówka","skoki narciarskie","koszykówka"]
# print(listasportow)
# listasportow.reverse()
# print(listasportow)
# listasportow.insert(7,"hokej")
# listasportow.insert(8,"tenis")
# print(listasportow)

#zad2
# slownikskrotow={"tzn.": "to znaczy","itp.": "i tym podobne","itd":"i tak dalej","tj.":"to jest"}
# print(slownikskrotow)
#
# print(slownikskrotow.keys())
# print(slownikskrotow.values())

#zad3
# slownikgier={"CS:GO":"Counter-Strike:Global-Offensive","WoW":"World of Warcraft","MC":"Minecraft"}
# print(slownikgier.keys())
# print(slownikgier.values())
# ilosc=len(slownikgier)
# print("W słowniku znajdują się", ilosc,"elementy.")

# #zad4
# zdanie= input("Podaj dowolne zdanie:")
# x=zdanie.count('a')
# y=zdanie.count('A')
# print("W tym zdaniu litera 'a' występuje",x,"razy.")
# print("W tym zdaniu litera 'A' występuje",y,"razy.")

#zad5
# system.stdout.write("Wprowadz 3 liczby calkowite: ")
# x = int(system.stdin.readline())
# y = int(system.stdin.readline())
# z = int(system.stdin.readline())
# H=(pow(x,y)+z)
# print("Wynik wynosi:",H)

#zad6
# system.stdout.write("Wprowadz 3 liczby calkowite: ")
# a = int(system.stdin.readline())
# b = int(system.stdin.readline())
# c = int(system.stdin.readline())
# if((a>=b) & (a>=c)):
#     print("Największa liczba to:",a)
# elif((b>=c) & (b>=a)):
#     print("Największa liczba to:", b)
# elif((c>=b) & (c>=a)):
#     print("Największa liczba to:", c)

#zad7
# lista=[7.30, 5, 4.14, 8, 13, 17, 91.20]
# for x in lista:
#     print(pow(x,2))

#zad8

# lista = []
# i=0
# while i!=10:
#     x=int(input("Podaj liczbe:"))
#     i+=1
#     if (x%2==0):
#         lista.append(x)
# print(lista)

#zad9

# lista=[1,2,3,4,5,6]
# for i in range(1,6):
#     if(i%2==1):
#         print("EEEEEE")
#     elif(i%2==0):
#         print("E")

#zad 10

a = float(input('Podaj liczbę: '))

try:
    print("Pierwiastek z podanej liczby wynosi:",sqrt(a))
except ValueError :
    print("Pierwiastek z liczby ujemnej nie istnieje. ")







