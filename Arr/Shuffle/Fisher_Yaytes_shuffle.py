import random
cards = list(range(1,33))
n = len(cards)
counter = 0
while n>1:
    n-=1
    i = random.randint(0,n-1)
    cards[n],cards[i] = cards[i], cards[n]
    print(i,n,sep="||")
    print(cards)
    counter += 1
print(counter) 
