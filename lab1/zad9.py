wiek=int(input("ile uczestnik ma lat? "))

if (wiek > 0) and (wiek < 150):
    #bedziemy wyceniac bilety
    if wiek < 4:
        print("Wchodzi za darmo.")
    elif wiek < 18:
        print("cena biletu to 10zl.")
    else:
        student= input("czy studiuje? (tak/nie).")
        if student == "tak":
            print("cena biletu to 15zl.")
        else:
            print("cena biletu to 20zl.")
else:
    print("nieprawidlowe dane")


