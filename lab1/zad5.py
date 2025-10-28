a = float(input("podaj dlugosc pirwszego boku:"))
b = float(input("podaj dlugosc drugiego boku:"))
#print(a)
#print(type(a))
#print(a+a)

pole = a*b
obw = 2*(a+b)
print(f"pole prostokata o wymiarach {a} na {b} wynosi: {pole}, a jego obwod obnosi {obw}. ")



#zadanie 6
droga = float(input("Droga pokonana przez samolot (km): "))
paliwo = float(input("Sreanie spalenie (w litrach na 100km): "))

spPaliwo = paliwo * droga / 100
cena = 6.5 * spPaliwo

print("Spalone paliwo {spPaliwo} l")
print(f"Cena {cena} : zl/l")
