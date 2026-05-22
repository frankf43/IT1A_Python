# Očekávané řešení žáků:
def spocitej_lektvary(inventar):
    pocet = 0
    for vec in inventar:
        if vec == "Lektvar":
            pocet = pocet + 1
    return pocet

batoh = ["Meč", "Lektvar", "Štít", "Lektvar", "Zlato"]
print("Máš lektvarů:", spocitej_lektvary(batoh))