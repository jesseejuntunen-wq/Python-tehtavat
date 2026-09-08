luku = int(input("anna kokonaisluku"))

alkuluku = True 

for i in range (2, luku):
    if luku % i == 0:
        alkuluku = False

if alkuluku:
    print("on alkuluku")
else:
    print("ei oo alkuluku")