print("Zadejte prvni cislo")
x:int = input()
print("Zadejte druhe cislo")
y:int = input() #datový typ není statický, pouze se jedná o HINT
if x > y:
    print(x + " je větší než " + y)
elif x == y:
    print("Zadana cisla jsou stejna")
else:
    print(y + " je větší než " + x)