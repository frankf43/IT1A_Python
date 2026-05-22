def vytvor_hrace(jmeno):
    # Vytvoření slovníku s vlastnostmi (klíč : hodnota)
    hrac = {
        "jmeno": jmeno,
        "zivoty": 100,
        "sila": 15
    }
    return hrac

muj_hrac = vytvor_hrace("Karel")

# Jak přečíst jen jednu konkrétní hodnotu:
print("Zrodil se hrdina:", muj_hrac["jmeno"])
print("Má životů:", muj_hrac["zivoty"])