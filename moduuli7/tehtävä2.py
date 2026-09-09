nimi = set()

while True:
    nimi2 = input("anna nimesi")
    if nimi2 == "":
        break
    else:
        if nimi2 in nimi:
         print("nimi on aijemmin syötetty")
        else:
                print("nimesi on uusi")
                nimi.add(nimi2)
                print(nimi2)

for nimi2 in nimi:
    print (nimi2)