import random

cards = list(range(1,33))
print(cards)

for i in range(len(cards)-1,0,-1):
    rand = random.randint(0,i)
    cards[i],cards[rand] = cards[rand], cards[i]
    print(cards)