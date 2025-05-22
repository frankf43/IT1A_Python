while True:
    clen1 = int(input("Zadejte první člen: "))
    clen2 = int(input("Zadejte druhý člen: "))

    """
    print("1. Soucet")
    print("2. Soucet")
    print("3. Soucet")
    print("4. Soucet")
    """
    while True:
        print("1. Součet \n2. Součin \n3. Rozdíl \n4. Podíl")
        operace = int(input("Vyberte číslo operace, kterou chcete provést: "))
        match operace:
            case 1:
                soucet = clen1 + clen2
                print("Součet je: " + str(soucet))
            case 2:
                soucin = clen1 * clen2
                print("Součin je: " + str(soucin))
            case 3:  
                rozdil = clen1 - clen2
                print("Rozdíl je: " + str(rozdil))
            case 4:
                if clen2 == 0:
                    print("Nelze dělit nulou.")
                else:    
                    podil = clen1 / clen2
                    print("Podíl je: " + str(podil))
                    
        konec = input("Přejete si nějakou další operaci pro člěny " + str(clen1) + " a " + str(clen2) + "? Y/N")
        if konec == "N" or konec == "n":
            break    
    konec = input("Přejete si ukončit program? Y/N")
    if konec == "Y" or konec == "y":
        break    

    