max = -1
for i in range(10):
    print("Zadejte cislo")
    cislo = int(input()) #nejprve nechat naletět, že nejde porovnávat int a string
    if cislo > max:
        max = cislo
print("Největší zadané číslo bylo " + str(max)) #nejprve nechat naletět bez přetypování