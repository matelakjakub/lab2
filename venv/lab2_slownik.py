slownik = {1: 22, "s": "a", 4.5: 10, 1:23}
print(slownik)

slownik['6'] = 1.1
print(slownik)

print(slownik[4.5])

slownik.pop(4.5)
print(slownik)

print(slownik.keys())

print(slownik.values())

del slownik["s"]
print(slownik)