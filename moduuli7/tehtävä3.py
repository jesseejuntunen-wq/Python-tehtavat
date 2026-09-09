asemat = {}
while True:
    print("1 = uus lentoasema")
    print("2 = hakea lentoasema tiedot")
    print("3 = Lopeta")

    valinta = input()

    if valinta == "1":
        icao = input("anna ICAO-koodi")
        nimi = input("anna lentoaseman nimi")
        asemat[icao] = nimi

    elif valinta == "2":
         icao2 = input("anna ICAO-koodi")
         if icao2 in asemat:
             print(asemat[icao])
         else:
             print("ei löydy")
        
    elif valinta == "3":
        break