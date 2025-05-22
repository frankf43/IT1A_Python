myList = ["pomeranč","jablko","citrón","kumqat","meloun","švestka","banán","kiwi"]

print(len(myList))
print(myList)
print(myList[1])
#print(myList[int(input("Zadejte číslo prvku v poli, který chcete vypsat."))]) #schválně zkuste zadat číslo mimo rozsah
print(myList[-1]) # mínus počítá od konce
dupList = myList[2:5] #včetně začátku a bez konce. Vynecháním začneme od začátku, nebo pojedeme až do konce. Když dám jen : vrátí všechno. Vytváří nový list
print(dupList)

if "jablko" in myList:
    print("Jablko tam je!")
print(myList)
myList[-2] = "Samice Hrabáče" 
#je možné používat i náhrady za rozsahy, pokud rozsah bude menší než počet nahrazovaných, list se rozšíří
#když by jich bylo míň tak se naopak list zkrátí
print(myList)

myList.append("grep") #přidá na konec
print(myList)
myList.insert(1,"ananas") #přidá prvek na místo kam řekneme, ale nic nezmizí
print(myList)

zeleninaList = ["paprika", "mrkev", "okurka"]
myList.extend(zeleninaList) #přidá list na konec listu
print(myList)

myList.remove("ananas") #odstraní prvek podle jeho obsahu. V případě vícenásobného výskytu odstraní jen první výskyt.
print(myList)

myList.pop(2) #odstraní konkrétní index. Když se nechá prázdný, odstraní poslední.
print(myList)

print(zeleninaList)
zeleninaList.clear() #vyprázdní list
print(zeleninaList)

del zeleninaList #definitivně odstraní list
#print(zeleninaList)

#VYPSÁNÍ OBSAHU POLE
for i in myList:
    print(i)

#VYPSÁNÍ PODLE INDEXŮ
for i in range(len(myList)):
    print(myList[i])

#SEŘAZENÍ PODLE ABECEDY
abeceda = ["A","F","C","D"]
abeceda.sort()
print(abeceda)

abeceda.sort(reverse=True)
print(abeceda)

#POZOR JE CASE SENSITIVE
myList.sort()
print(myList)

myList.sort(key=str.lower)
print(myList)


#SEŘAZENÍ PODLE HODNOTY
nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

#PŘEHOZENÍ POŘADÍ
print(myList)
myList.reverse()
print(myList)


#COPY
myList2 = myList

print(myList)
myList2[0] = "rajče"
print(myList)

#je nutné na to jít jinak
copyList = myList.copy()
copyList[0] = "ořech"
print(myList)
print(copyList)