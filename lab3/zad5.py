# try
zakupy = {}
liczba = int(input("Liczba zakupów: "))
for i in range(liczba):
    artykul = input("Podaj artykul: ")
    while True:
        try:
            kwota = int(input("Podaj kwota: "))
            break
        except ValueError:
            print("To nie jest liczba, spróbuj ponownie.")
    zakupy[artykul] = kwota
for key, value in zakupy.items():
    print(key, value, sep=" - ")
print(sum(zakupy.values()))