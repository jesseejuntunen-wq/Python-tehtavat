käyttäjätunnus = input("anna käyttäjätunnus")
salasana = input("anna salasana")

while True:
    if käyttäjätunnus == "python" and salasana == "rules":
        print("tervetuloa")
    else:
        print("pääsy evätty")

        käyttäjätunnus2 = input("anna käyttäjätunnus")
        salasana2 = input("anna salasana")

        if käyttäjätunnus2 == "python" and salasana2 == "rules":
            print("tervetuloa")
        else:
            käyttäjätunnus3 = input("anna käyttäjätunnus")
            salasana3 = input("anna salasana")

            if käyttäjätunnus3 == "python" and salasana3 == "rules":
                print("tervetuloa")
            else:
                käyttäjätunnus4 = input("anna käyttäjätunnus")
                salasana4 = input("anna salasana")

                if käyttäjätunnus4 == "python" and salasana4 == "rules":
                    print("tervetuloa")
                else:
                    käyttäjätunnus5 = input("anna käyttäjätunnus")
                    salasana5 = input("anna salasana")

                    if käyttäjätunnus5 == "python" and salasana5 == "rules":
                        print("tervetuloa")
                    else:
                        print("pääsy evätty lopullisesti")

    break