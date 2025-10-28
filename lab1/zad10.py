# Program porządkowania trzech liczb bez użycia funkcji sortujących

# Pobranie danych od użytkownika
x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

# Porządkowanie liczb
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

# Wynik
print("Liczby w kolejności rosnącej:", x, y, z)

