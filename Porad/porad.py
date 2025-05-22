cislo = int(input())
soucet = cislo
while cislo > 0:
    print("Zadali jste " + str(cislo) + ". Co dal?")
    cislo = int(input())
    if cislo > 0:
        soucet += cislo
print("Celkovy soucet cisel je " + str(soucet))
