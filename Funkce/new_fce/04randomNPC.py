import random

def vygeneruj_nepritele(jmeno):
    druhy = ["Skřet", "Troll", "Vlk"]
    druh = random.choice(druhy)
    zivoty = random.randint(20, 100)
    
    return "Nepřítel " + jmeno + " je " + druh + " a má " + str(zivoty) + " HP."

print(vygeneruj_nepritele("Gorg"))
print(vygeneruj_nepritele("Bax"))