# Collatzův problém
# Mějme přirozené číslo. Pokud je sudé, vydělíme jej dvěma, pokud je liché, vynásobíme jej 3 a přičteme 1. 
# To opakujeme dokud nedostaneme 1. 
# Spočítejte počet průchodů nutných pro vyřešení problému a vypisujte průběžné výsledky.


while(True):
    x = int(input("Zadejte číslo: "))
    if x > 0:
        break
counter = 0
while (x != 1):
    print(x)
    if x % 2 == 0:
        x=x/2
        counter+=1
    else:
        x=(x*3)+1
        counter+=1
print("Pro vyřešení problému bylo potřeba " + str(counter) + " průchodů.")