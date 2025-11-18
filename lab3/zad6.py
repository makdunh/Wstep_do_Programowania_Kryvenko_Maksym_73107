rachunki = {
    "styczeń": 190,
    "luty": 205,
    "marzec": 210,
    "kwiecień": 235,
    "maj": 215
}
# A
print("Maxsymalna wartość:", max(rachunki.values()))
print("Minimalna wartość:", min(rachunki.values()))
print("Suma wartośći:", sum(rachunki.values()))
srednia = sum(rachunki.values())/len(rachunki)
print("Wartość średnią:", srednia)

# B
ostatni_miesiac = list(rachunki.keys())[-1]  # беремо останній місяць
if rachunki[ostatni_miesiac] > srednia:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")