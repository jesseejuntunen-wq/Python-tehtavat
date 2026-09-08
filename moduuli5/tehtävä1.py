import random
noppa = int(input("montas noppaa heitetää"))
lasku = 0
for i in range (noppa):
    heitto = random.randint(1,6)
    lasku += heitto
print(lasku)