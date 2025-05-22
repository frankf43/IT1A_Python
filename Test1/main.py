while True:
    tvar = input("S jakým tvarem si přejete pracovat?")
    match tvar:
        case "obdélník":
            while True:
                a = input("Zadejte délku strany a.")
                b = input("Zadejte délku strany b.")
                if a.isdigit() and b.isdigit():
                    a = int(a)
                    b = int(b)
                    break
                else:
                    print("Chybné zadání!")
            
            while True:
                operace = input("Jakou operaci si přejete provést?")
                
                if operace == "obvod":
                    obvod = 2*(a+b)
                    print("Obvod je " + str(obvod))
                    break
                elif operace == "obsah":
                    obsah = a*b
                    print("Obsah je " + str(obsah))
                    break
                else:
                    print("Chybné zadání!")
        case "čtverec":
            while True:
                strana = input("Zadejte délku strany.")
                if strana.isdigit():
                    strana = int(strana)
                    break
                else:
                    print("Chybné zadání!")
            
            while True:
                operace = input("Jakou operaci si přejete provést?")
                if operace == "obvod":
                    obvod = strana*4
                    print("Obvod je " + str(obvod))
                    break
                elif operace == "obsah":
                    obsah = strana*strana
                    print("Obsah je " + str(obsah))
                    break
                else:
                    print("Chybné zadání!")
        case "trojúhelník":    
            while True:
                a = input("Zadejte délku strany a.")
                b = input("Zadejte délku strany b.")
                c = input("Zadejte délku strany c.")
                if a.isdigit() and b.isdigit() and c.isdigit():
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    break
                else:
                    print("Chybné zadání!")
                    
            if a+b > c and a+c > b and c+b > a:
                print("Trojúhelník lze sestavit.")
                if a == b == c:
                    print("Trojúhelník je rovnostranný.")
                elif a == b or b == c or a == c:
                    print("Trojúhelník je rovnoramenný.")
                else:
                    print("Trojúhelník je obecný.")
            else:
                print("Takový trojúhelník nelze sestavit.")
        case _:
            print("Chybné zadání!")
    konec = input("Přejete si počítat dál? Pro pokračování stiskněte pouze enter.")
    if konec != "":
        print("Program se nyní ukončí.")
        break