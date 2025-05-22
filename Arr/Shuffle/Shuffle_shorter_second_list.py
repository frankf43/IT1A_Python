import random
cards = list(range(1,33))
shuffled = []
n = len(cards)
counter = 0

while n:
    n-=1
    i = random.randint(0,n)
    shuffled.append(cards.pop(i))
    print(cards)
    print(shuffled) 
    counter += 1
print(counter)