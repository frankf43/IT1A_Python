# Očekávané řešení žáků:

def proved_utok(utocnik, obrance):
    zraneni = utocnik["sila"]
    obrance["hp"] = obrance["hp"] - zraneni
    print(utocnik["jmeno"] + " útočí na " + obrance["jmeno"] + " a dává " + str(zraneni) + " poškození!")

moje_postava = {"jmeno": "Barbar", "sila": 15}

skreti = [
    {"jmeno": "Malý skřet", "hp": 20},
    {"jmeno": "Velký skřet", "hp": 40},
    {"jmeno": "Skřetí šaman", "hp": 25}
]

print("--- ZAČÍNÁ PLOŠNÝ ÚTOK ---")
# Cyklus projde seznam a na každého skřeta zavolá bojovou funkci
for skret in skreti:
    proved_utok(moje_postava, skret)
    
    # Kontrola, zda to skřet přežil
    if skret["hp"] <= 0:
        print(skret["jmeno"] + " byl poražen!")
    else:
        print(skret["jmeno"] + " přežil a zbývá mu " + str(skret["hp"]) + " HP.")
    print("------------------------")