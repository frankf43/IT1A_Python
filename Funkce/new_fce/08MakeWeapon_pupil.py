# Očekávané řešení žáků:
import random

def vytvor_zbran(material):
    typy = ["Meč", "Luk", "Hůl"]
    zbran = {
        "nazev": random.choice(typy),
        "material": material,
        "bonus": random.randint(1, 10)
    }
    return zbran

moje_zbran = vytvor_zbran("Železný")
print("Získal jsi:", moje_zbran["material"], moje_zbran["nazev"])
print("Poškození navíc:", moje_zbran["bonus"])