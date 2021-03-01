print("Proszę podać pierwszą liczbę: ")
a = input()
print("proszę podać drugą liczbę")
b = input()

try:
    wynik = int(a) / int(b)
    print(wynik)
except ZeroDivisionError:
    print("nie można podzielić przez 0 ")
