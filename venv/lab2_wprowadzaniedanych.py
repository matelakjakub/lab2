a = input ("podaj pierwszą liczbę: ")
b = input ("podaj drugą liczbę: ")
c = input ("podaj trzecią liczbę: ")
d = input ("podaj czwartą liczbę: ")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a > b) & (c>d):
    print("Liczba a jest wieksza od b i liczba c jest wieksza od d")
else:
    print("Liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d")