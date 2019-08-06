#pętla

pawel = "t"
while pawel == "t":

# zmienne
        obecny_rok = int(input("Podaj obecny rok: "))
        rok_python = 1989
        wiek_pythona = obecny_rok - rok_python

# dane usera
        imie = input("Jak masz na imię?: ")
        lata =  int(input("Ile masz lat?: "))

# komunikaty wyświetlane
        print("Witaj,", imie)
        print("Masz:", lata, "lat")
        print("-" * 40)

# przedstawienie sie przez pythona
        print("Nazywam się python, mam lat:", wiek_pythona)
        if(lata < wiek_pythona):
                print("jesteś ode mnie młodszy o: " , wiek_pythona - lata)
        elif(lata == wiek_pythona):
                print("masz tyle lat co ja! :)")
        else:
            if(lata > wiek_pythona):
                    print("jesteś ode mnie starszy o: ", wiek_pythona - lata)

        pawel = input("Czy chcesz wpisać dane jeszcze raz? t/n")

print("koniec skryptu")
