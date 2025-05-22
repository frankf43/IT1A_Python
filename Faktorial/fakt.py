fakt = int(input("Zadejte číslo, jehož faktoriál chcete.")) 
vysledek = 1 #nejprve klidně int, ale přeteče
for i in range(1,fakt+1):
    vysledek *= i
    print(vysledek)
print(vysledek)