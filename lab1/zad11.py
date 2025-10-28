# Program rozwiązywania równania kwadratowego ax^2 + bx + c = 0

import math

# Pobranie współczynników od użytkownika
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Sprawdzenie, czy to faktycznie równanie kwadratowe
if a == 0:
    # Równanie liniowe bx + c = 0
    if b != 0:
        x = -c / b
        print("Równanie jest liniowe. Rozwiązanie: x =", x)
    else:
        if c == 0:
            print("Równanie tożsamościowe — nieskończenie wiele rozwiązań.")
        else:
            print("Równanie sprzeczne — brak rozwiązań.")
else:
    # Obliczenie delty
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Dwa rozwiązania rzeczywiste:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Jedno rozwiązanie (podwójny pierwiastek): x =", x)
    else:
        # Delta < 0 — brak rozwiązań rzeczywistych
        re = -b / (2*a)
        im = math.sqrt(-delta) / (2*a)
        print("Brak rozwiązań rzeczywistych.")
        print(f"Rozwiązania zespolone: x1 = {re} - {im}i, x2 = {re} + {im}i")


