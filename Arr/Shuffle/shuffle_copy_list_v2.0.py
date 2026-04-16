import random

cards = list(range(1,33))
shuffled = []
print(cards)

while cards:
    shuffled.append(cards.pop(random.randint(0,len(cards)-1)))

print(cards)
print(shuffled)