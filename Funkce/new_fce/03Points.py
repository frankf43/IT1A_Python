def spocitej_skore(seznam_bodu):
    celkem = 0
    for body in seznam_bodu:
        celkem = celkem + body
    return celkem

moje_body = [10, 50, 5, 20]
print("Celkové skóre je:", spocitej_skore(moje_body))