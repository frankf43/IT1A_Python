import random
counter = 0
while True:
    num = int(input("Zadejte číslo"))
    if 0 < num < 7:
        break

while True:
    kostka1 = random.randint(1,6)
    kostka2 = random.randint(1,6)
    print(str(kostka1) +" "+ str(kostka2))

    counter += 1
    """if kostka1 == kostka2 and kostka1 == num:
        break"""

    if kostka1 == kostka2 == num:
        break

print("Počet nutných pokusů byl: " + str(counter))