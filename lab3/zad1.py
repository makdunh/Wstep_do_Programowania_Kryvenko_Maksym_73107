imiona = ["Krzysiek", "Pawel", "Michal", "Kamil"]
print(imiona)

for i in imiona:
    print(i)

    for i in range (len(imiona)):
        print(f"index: {i}, imie: {imiona[i]}")

#A ver1
print(sorted(imiona))
#ver2
posortowane_imiona= sorted(imiona)
print(posortowane_imiona)

#B
imiona.append("Kasia")
imiona.append("Ala")
print(imiona)

print(imiona.pop())
print(imiona)

#C
imiona.insert(3, "Basia")
print(imiona)

#D
imiona.reverse()
print(imiona * 2)

