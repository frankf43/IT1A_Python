while True:
    cislo = input("Zadejte číslo: ")
    if cislo.lstrip("-").isdigit():
        max = int(cislo)
        break
    else:
        print("Nezadali jste číslo!")
while cislo.lstrip("-").isdigit():                      #můžeme vylepšit, aby pro ukončení bylo potřeba písmeno K, případně tradiční dialog Chcete ukončit Y/N
    print("Momentální maximum je:" + str(max))
    cislo = input("Zadejte číslo: ")
    if cislo.lstrip("-").isdigit() and max < int(cislo):
        max = int(cislo)
    konec = input("Přejete si zadat další číslo? (Pro ukončení zadejte N, jinak potvrďte) ")
    if konec == "N":
        break
print("Největší zadané číslo bylo " + str(max))