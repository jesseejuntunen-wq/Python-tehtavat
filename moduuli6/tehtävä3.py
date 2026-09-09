def lasku(gallon):
    return gallon * 3.785


while True:
    gallon = float(input("anna gallonmäärä"))
    if gallon < 0 :
        break

    litra = lasku(gallon)
    print (f"liramäärä on {litra}")