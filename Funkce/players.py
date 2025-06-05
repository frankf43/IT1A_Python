import random

def player(name:str):

    myList=["Útočník", "Obránce", "Golman"]

    print(name + " "+ myList[rand(len(myList)-1)])
    #return name + " útočník"
'''
print(player("Jiří"))
print(player("Honza"))
print(player("Bedřich"))
print(player("Zdeněk"))
'''
def rand(pole:int):
    return random.randint(0,pole)

player("Jiří")
player("Honza")
player("Bedřich")
player("Zdeněk")

