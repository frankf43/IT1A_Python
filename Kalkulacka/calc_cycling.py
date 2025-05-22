while(True):
    clen1 = int(input("Zadejte první člen: "))
    clen2 = int(input("Zadejte druhý člen: "))

    soucet = clen1 + clen2
    soucin = clen1 * clen2
    rozdil = clen1 - clen2
    podil = clen1 / clen2

    print("Součet je: " + str(soucet))
    print("Součin je: " + str(soucin))
    print("Rozdíl je: " + str(rozdil))
    if clen2 == 0:
        print("Nelze dělit nulou.")
    else:    
        print("Podíl je: " + str(podil))
    konec = input("Přejete si ukončit program? Y/N")
    if konec == "Y" or konec == "y":
        break    

    