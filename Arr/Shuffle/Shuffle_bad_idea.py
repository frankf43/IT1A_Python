import random
cards = list(range(1,33))
shuffled = []
n = len(cards)
counter=0

while n:
    i = random.randint(0,len(cards)-1)
    if(cards[i] != 0):
        shuffled.append(cards[i])
        cards[i]=0
        n -= 1
    
    counter+=1
print(cards)
print(shuffled)
print(counter)


