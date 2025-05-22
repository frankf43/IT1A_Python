clen1 = int(input("Zadejte první člen."))
clen2 = int(input("Zadejte druhý člen."))

soucet = clen1 + clen2
soucin = clen1 * clen2
rozdil = clen1 - clen2
podil = clen1 / clen2

print(soucet)
print(soucin)
print(rozdil)
if clen2 == 0:
    print("Nelze dělit nulou.")
else:    
    print(podil)
