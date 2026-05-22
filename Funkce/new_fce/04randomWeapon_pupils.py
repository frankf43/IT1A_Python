# Očekávané řešení žáků:
import random

def vytvor_zbran(material):
    typy_zbrani = ["Meč", "Luk", "Hůl"]
    typ = random.choice(typy_zbrani)
    bonus = random.randint(1, 10)
    
    return material + " " + typ + " (+ " + str(bonus) + " k poškození)"

print(vytvor_zbran("Železný"))
print(vytvor_zbran("Dřevěný"))