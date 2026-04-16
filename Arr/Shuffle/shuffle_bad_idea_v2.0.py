import random

cards = list(range(1,33))
shuffled = []
inkr = 0
print(cards)
for _ in range(32):
    while True:
        inkr += 1
        card = random.randint(0,31)
        if cards[card] != None:
            shuffled.append(cards[card])
            cards[card] = None
            break
print(shuffled)
print(cards)
print(inkr)