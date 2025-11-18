import random

n = int(input("Podaj n: "))
x = int(input("Podaj x: "))
s = int(input("Podaj s: "))

lista = []

for i in range(n):
    slowo = ""
    for j in range(random.randint(1, x)):
        slowo += chr(random.randint(97, 122))   # losowa litera a-z
    lista.append(slowo)

print("Lista:", lista)

krotka = tuple(lista)
print("Krotka:", krotka)


# A
print("Ilość znaków w liście:", sum(len(slowo) for slowo in lista))

#B
liczba_k = "k"
lb_w = 0

for slowo in krotka:
    for znak in slowo:
        if znak == liczba_k:
            lb_w += 1

print("Ilość 'k' w krotce:", lb_w)

#C
liczba_kt = "kt"
lb_kt = 0

for slowo in krotka:
    if liczba_kt in slowo:
        lb_kt += 1

print("Ilość 'kt' w krotce:", lb_kt)

#D
liczba_dw = 0
for slowo in krotka:
    if len(slowo) > s:
        liczba_dw += 1
print(liczba_dw)