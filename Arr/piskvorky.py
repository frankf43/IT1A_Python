pole=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def vykresli_pole(pole):
    for radek in pole:
        print("| " + " | ".join(radek) + " |") #Join slepuje dohromady věci z listu první | je levý okraj, pak se vyrobí | oddělené věci v listu a | na konci je pravý okraj

hrac = "X"
tahy = 0
vykresli_pole(pole)
while tahy < 9:
    print(f"Hraje hráč {hrac}")
    
    r = int(input("Zadej řádek (0-2): "))
    s = int(input("Zadej sloupec (0-2): "))
    
    if pole[r][s] == " ":
        pole[r][s] = hrac
        tahy += 1
        # Tady by měla následovat kontrola vítěze
        hrac = "O" if hrac == "X" else "X"
        vykresli_pole(pole)
    else:
        print("Tohle pole už je obsazené!")

print("Konec hry!")