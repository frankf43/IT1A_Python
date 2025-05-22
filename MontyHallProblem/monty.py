import random
win = 0
lose = 0
iterations = int(input("Zadejte počet opakování, který chcete simulovat."))
for i in range(iterations):
    car = random.randint(1,3)
    playersChoice = random.randint(1,3)
    while True:
        montysChoice = random.randint(1,3)
        if montysChoice != car and montysChoice != playersChoice:
            break
    playersOld = playersChoice
    while True:
        playersChoice=random.randint(1,3)
        if playersChoice != playersOld and playersChoice != montysChoice:
            break
    if playersChoice == car:
        win += 1
    else:
        lose += 1
    print(i)
#f string neřeší datové typy a umožňuje provádět i nejrůznější úpravy, operace a funkce
print(f"Hráč prohrál v {lose} případech a zvítězil v {win} případech \nto znamená, že zvítězil v {((win / iterations) * 100):.2f} % případů a prohrál v {((lose / iterations) * 100):.2f} % případů." )
