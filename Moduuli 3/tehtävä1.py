kuha = float(input("anna kuhan mitta"))
if kuha < 37.0:
    print("liian pieni heitä järvee")
    lasku = 37.0 - kuha
    print("kuhan pituudesta puuttuu", lasku)
elif kuha >= 37.0:
    print("kuha on hyvä")
