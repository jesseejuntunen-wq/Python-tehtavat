tuuma = 2.4

while True:
    Tuuma = float(input("anna tuuma määrä")) 
    lasku = Tuuma * tuuma
    if lasku <= 0:
        break
    elif lasku:
        print(lasku)