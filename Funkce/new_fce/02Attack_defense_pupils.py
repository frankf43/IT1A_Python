# Očekávané řešení žáků:
def vyhodnot_souboj(utok, obrana):
    if utok > obrana:
        return "Zásah!"
    else:
        return "Zblokováno!"

print(vyhodnot_souboj(50, 30))
print(vyhodnot_souboj(20, 40))