import random
import os

#player / enemy stats
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

#skills.  Need to add player choice logic
skill_list = [
    "Hide",
    "Flee",
    "Cower",
    "Nutpunch",
    "Disgust",
    "Beg",
    "Flail",
]

#example encounter stats
p1 = Player("Florbert The Unseemly",20)
p1.skills = ["Hide","Cower","Disgust"]
enemy = Enemy("Annoyed Donkey")
enemy.weaknesses = "Flail"
enemy.resistances = "Cower"

#game mechanics
class Encounter:
    def __init__(self,encounternum):
        self.encounternum = encounternum
        self.encountertext = []
        nextencounter = encounternum + 1
        prevencounter = encounternum - 1

def yourchoice():
    return int(input("Your choice: "))

#random logic for skill text goes here
def flail():
    flail_text = [
        "You hammer your fists wildly at the ",
        "You let loose an anguished cry and flail at the ",
        "You raise your hands above your head in a threatening gesture and flail at the ",
    ]
    return f'{random.choice(flail_text)}{enemy.name}'

#

#game encounters
e1 = Encounter(1)
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
            print(f'{flail()}.  It looks at you with what appears to be confusion and slowly saunters down the road')
            nextencounter()

#testing
encounter1()







