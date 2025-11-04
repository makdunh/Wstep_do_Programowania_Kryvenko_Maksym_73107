lb_w =int(input("podaj liczbe wierszy:"))

for i in range(lb_w):
    for j in range(lb_w-(lb_w-(i+1))):
        print("* ", end="")
    print("")

