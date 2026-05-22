# Očekávané řešení žáků:
def zaplat_zlato(inventar, castka):
    if inventar["Zlaťáky"] >= castka:
        inventar["Zlaťáky"] = inventar["Zlaťáky"] - castka
        print("Zaplaceno", castka, "zlaťáků.")
        
    else:
        print("Nemáš dost peněz!")
        

hracuv_batoh = {"Zlaťáky": 100, "Meč": 1}

# Zkouška funkce
zaplat_zlato(hracuv_batoh, 40)
print("Zbývá ti:", hracuv_batoh["Zlaťáky"])
zaplat_zlato(hracuv_batoh, 200) # Zde by měla vyskočit chyba