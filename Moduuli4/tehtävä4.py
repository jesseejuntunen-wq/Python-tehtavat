import random
luku = random.randint(1,10)

while True:
    numero =  int(input("arvaappa numero"))
    if numero < random.randint(1,10):
        print ("liian pieni")
    elif numero > random.randint(1,10):
        print("luku liian suuri")

    else: 
     
        print("jackpot jahhuu ")
        break
