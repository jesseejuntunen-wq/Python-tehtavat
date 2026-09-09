def lasku(lista):
    lista2 = []
    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    return lista2
lista = [1,2,3,4,5]
tulos = lasku(lista)
print (tulos)