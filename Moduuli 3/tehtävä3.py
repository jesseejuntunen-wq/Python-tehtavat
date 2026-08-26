sukupuoli = input("anna sukupuolesi")
hemo = float(input("anna hemoglobiini arvosi (gl)"))
if sukupuoli == "nainen" and hemo >= 117 and hemo <= 175:
    print("hemoglobiini on normaali")
elif sukupuoli == "nainen" and hemo > 175:
    print("hemoglobiinisi on korkea")
elif sukupuoli == "nainen" and hemo < 117:
    print("alhainen hemoglobiini")
elif sukupuoli == "mies" and hemo >= 134 and hemo <= 195:
    print("hemoglobiinisi on normaali")
elif sukupuoli == "mies" and hemo > 195:
    print("hemoglobiinisi on korkea")
elif sukupuoli == "mies" and hemo < 134:
    print("alhainen hemoglobiini")