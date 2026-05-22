# Funkce dělá jen logiku: zkontroluje peníze, případně je odečte a vrátí výsledek.
def zaplat(postava, cena):
    if postava["zlato"] >= cena:
        postava["zlato"] = postava["zlato"] - cena
        return True
    else:
        return False

hrac = {"jmeno": "Ragnar", "hp": 50, "zlato": 25}
hra_bezi = True

# Hlavní smyčka drží hru v chodu a řeší vstupy
while hra_bezi == True:
    print(f"\nHráč: {hrac['hp']} HP | {hrac['zlato']} Zlato")
    volba = input("Koupit léčení za 10z [1], Trénink za 20z [2] nebo Konec [3]? ")
    
    if volba == "1":
        # Zavoláme funkci. Pokud vrátí True, platba prošla a přidáme HP.
        if zaplat(hrac, 10) == True:
            hrac["hp"] = hrac["hp"] + 20
            print("Úspěšně ses vyléčil!")
        else:
            print("Na léčení nemáš peníze!")
            
    elif volba == "2":
        # Stejnou funkci použijeme znovu pro úplně jiný nákup!
        if zaplat(hrac, 20) == True:
            print("Skvělý trénink, cítíš se silnější!")
        else:
            print("Trenér tě vyhodil, nemáš dost zlata.")
            
    elif volba == "3":
        hra_bezi = False