import random
import os

class Player:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.equipment = []
        self.gold = 0
        self.skills = []

class Enemy:
    def __init__(self,name):
        self.name = name
        self.resistances = []
        self.weaknesses = []
        
skill_list = [
    "Hide",
    "Flee",
    "Cower",
    "Nutpunch",
    "Disgust",
    "Beg",
    "Flail",
]

p1 = Player("Florbert The Unseemly",20)
p1.skills = ["Hide","Cower","Disgust"]
enemy1 = Enemy("Annoyed Donkey")
enemy1.weaknesses = "Flail"

def yourchoice():
    int(input("Your choice: "))

def prevencounter():
    return 


def encounter1():
    print(f'''
    Walking down the path, you see a large gray donkey in the middle of the road.  It doesn't appear to be interested in moving any time soon.

    If you choose to flee from the donkey and return the way you came, press 1
    If you choose to hide in the bushes beside the road until it leaves, press 2
    If you choose to flail wildly against the donkey with your fists, press 3
    ''')
    while True:
        choice = yourchoice()
        if choice == 1:
            print('You turn away and go back the way you came')
            prevencounter()
        elif choice == 2:
            print('You wait for several hours in the bug-infested reeds.  The donkey does not move')
            continue
        elif choice == 3:
            print('You scream and hammer at the donkey wildly with your fists.  It looks at you with what appears to be confusion and slowly saunters down the road')
            nextencounter()
            










