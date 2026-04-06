while True:
    choice = input("Zadejte tvar s kterým chcete pracovat. Obdélník/Čtverec/Trojúhelník --> ").lower()
    match choice:
        case "obdélník":
            a = int(input("Zadejte stranu A: "))
            b = int(input("Zadejte stranu B: "))
            operation = input("Přejete si obvod nebo obsah? ")
            match operation:
                case "obvod":
                    print(f"Obvod vašeho obdélníku je {2*(a+b)}")
                case "obsah":
                    print(f"Obsah vašeho obdélníku je {a*b}")
                case _:
                    print("Neplatná volba.")
        case "čtverec":
            a = int(input("Zadejte stranu A: "))
            operation = input("Přejete si obvod nebo obsah? ")
            match operation:
                case "obvod":
                    print(f"Obvod vašeho čtverce je {4*a}")
                case "obsah":
                    print(f"Obsah vašeho čtverce je {a*a}")
                case _:
                    print("Neplatná volba.")
        case "trojúhelník":
            a = int(input("Zadejte stranu A: "))
            b = int(input("Zadejte stranu B: "))
            c = int(input("Zadejte stranu C: "))
            if a + b > c and a + c > b and c + b > a:
                print("Výborně trojúhelník lze sestavit!")
                if a == b or b == c or c == a:
                    if a == b == c:
                        print("Trojúhelník je rovnostranný.")
                    else:
                        print("Trojúhelník je rovnoramenný.")
                else:
                    print("Trojúhelník je obecný.")
            else:
                print("Bohužel, tento trojúhelník nelze sestavit.")
        case _:
            print("Neplatné zadání.")
    if input("Přejete si pokračovat? Y/N --> ").upper() != "Y":
        print("Ukončuji program.")
        break