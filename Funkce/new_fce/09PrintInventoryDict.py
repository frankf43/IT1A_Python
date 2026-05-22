def vypis_batoh(inventar):
    print("\n--- TVŮJ BATOH ---")
    # Cyklus projde všechny klíče (názvy předmětů) ve slovníku
    for predmet in inventar:
        pocet = inventar[predmet]
        print(f"- {predmet}: {pocet} ks")
    print("------------------")

muj_batoh = {
    "Lektvar zdraví": 3,
    "Zlaťáky": 150,
    "Pochodeň": 1
}

vypis_batoh(muj_batoh)