import random
counter = 0
while True:
    kostka1 = random.randint(1,6)
    kostka2 = random.randint(1,6)
    print(str(kostka1) +" "+ str(kostka2))

    if kostka1 != kostka2:
        counter += 1
    else:
        break

print("Počet nutných pokusů byl: " + str(counter))