max = int(input("Zadejte číslo: "))
for i in range(9):
    cislo = int(input("Zadejte číslo: ")) #nejprve nechat naletět, že nejde porovnávat int a string
    if cislo > max:
        max = cislo
print("Největší zadané číslo bylo " + str(max)) #nejprve nechat naletět bez přetypování