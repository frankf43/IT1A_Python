"""clen1 = int(input("Zadejte první člen."))
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
    print(podil)"""

def main():
    clen1 = int(input("Zadejte první člen."))
    clen2 = int(input("Zadejte druhý člen."))
    print(soucet(clen1,clen2))

def soucet(a:int, b:int):
    soucet = a + b
    return soucet

main()

def nasobeni():
    clen1 = int(input("Zadejte člen 1: "))
    clen2 = int(input("Zadejte člen 2"))
    vysledek = 0
    for i in range(clen2):
        vysledek = soucet(clen1, vysledek)
    return vysledek
print(nasobeni())



