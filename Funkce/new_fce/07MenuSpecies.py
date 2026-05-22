import random

def zobraz_menu():
    print("--- HLAVNÍ MENU ---")
    print("1 - Vytvořit postavu")
    print("2 - Konec hry")

def vygeneruj_nepritele(jmeno):
    druhy = ["Skřet", "Troll", "Vlk"]
    druh = random.choice(druhy)
    zivoty = random.randint(20, 100)
    
    return "Nepřítel " + jmeno + " je " + druh + " a má " + str(zivoty) + " HP."

hra_bezi = True # Tato proměnná řídí celou hru

while hra_bezi == True:
    zobraz_menu()
    volba = input("Co chceš udělat? (napiš číslo): ")
    
    if volba == "1":
        print(">> Generuji postavu...")
        print(vygeneruj_nepritele(input("Zadejte jméno.")))
    elif volba == "2":
        print(">> Vypínám hru. Ahoj!")
        hra_bezi = False # Smyčka skončí
    else:
        print(">> Špatná volba, zkus to znovu.")