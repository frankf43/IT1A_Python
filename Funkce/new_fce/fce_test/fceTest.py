def spocti_celkem(ceny):
    """Úroveň 1: Sečte položky v košíku bez použití sum()"""
    celkem = 0
    for cena in ceny:
        celkem += cena
    return celkem

def najdi_nejdrazsi(ceny):
    """Úroveň 2: Najde nejdražší položku bez použití max()"""
    if not ceny: # Ošetření pro prázdný košík
        return 0
        
    nejdrazsi = ceny[0]
    for cena in ceny:
        if cena > nejdrazsi:
            nejdrazsi = cena
    return nejdrazsi

def filtruj_drahe(ceny, limit):
    """Úroveň 3: Vrátí nový seznam pouze s položkami nad daný limit"""
    drazsi_polozky = []
    for cena in ceny:
        if cena >= limit:
            drazsi_polozky.append(cena)
    return drazsi_polozky

def aplikuj_slevu(ceny, sleva_procenta, limit_pro_slevu):
    """Úroveň 4: Zavolá spocti_celkem a případně aplikuje slevu"""
    celkova_cena = spocti_celkem(ceny)
    
    if celkova_cena >= limit_pro_slevu:
        sleva_hodnota = celkova_cena * (sleva_procenta / 100)
        return celkova_cena - sleva_hodnota
    else:
        return celkova_cena

# --- Testování kódu ---
muj_kosik = [120, 50, 200, 890, 15]

print("--- Výsledky ---")
# 1. úroveň
print(f"Celková cena nákupu: {spocti_celkem(muj_kosik)} Kč")

# 2. úroveň
print(f"Nejdražší položka stojí: {najdi_nejdrazsi(muj_kosik)} Kč")

# 3. úroveň
# Zkusíme vyfiltrovat položky, které stojí 200 Kč a více
print(f"Položky od 200 Kč výše: {filtruj_drahe(muj_kosik, 200)}")

# 4. úroveň
# Aplikujeme 10% slevu, pokud nákup přesáhne 1000 Kč
cena_po_sleve = aplikuj_slevu(muj_kosik, 10, 1000)
print(f"Konečná cena (případně po slevě): {cena_po_sleve} Kč")

input()