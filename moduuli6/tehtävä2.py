import random
tahko = int(input("montako tahkoa nopassa"))
def noppa():
    return random.randint(1,tahko) 
    
while True: 
    tulos = noppa()
    print(tulos)


    if tulos == tahko:
        break
        