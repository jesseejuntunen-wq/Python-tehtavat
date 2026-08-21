leiviska = float(input("anna leiviskät"))
naula = float(input("anna naulat"))
luoti = float(input("anna luodit"))

kauheetehtava = ((leiviska * 20 * 32) + (naula * 32) + luoti) * 13.3

gramma = (kauheetehtava  % 1000)
kilo = (kauheetehtava // 1000)

print(f"kiloja on {kilo} ja grammoja{gramma}")


