import random
import os

from numpy import choose

#because f strings don't like backslashes
newline = '\n'
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
        self.successtext = []
        self.failtext = []

#example encounter stats
p1 = Player("Florbert The Unseemly",20)
p1.skills = ["hide","cower","flail"]
donkey = Enemy("donkey")
donkey.successtext = "It looks at you with what appears to be confusion and slowly saunters down the road"
donkey.failtext = "It tramples you.  You die."
donkey.resistances = "cower"
donkey.weaknesses = "flail"
# skills.  Need to add player choice logic
skilllist = [
    "Hide",
    "Flee",
    "Cower",
    "Nutpunch",
    "Beg",
    "Flail",
]

# game mechanics
def yourchoice():
    return int(input("Your choice: "))

def chooseskills():
    while len(p1.skills) <= 3:
        for index, value in enumerate(skilllist, start=1):
            print(f'{index}: {value}')
        choice = input("Choose 3 Skills (press k for skill descriptions): ")
        if choice.lower() == 'k':
            for item in skilllist:
                print(f'{item}: {item.skilltext}')
        elif choice in skilllist:
            p1.skills.append(skilllist.pop(skilllist.index(choice-1)))
        else:
            print('Not a valid response')
            continue

class Encounter:
    def __init__(self,encounternum):
        self.encounternum = encounternum
        self.encountertext = []
        nextencounter = encounternum + 1
        prevencounter = encounternum - 1

class Skill:
    def __init__(self,skillname):
        self.skillname = skillname
        self.skilltext = " "
        self.skilloutcomes = []

# skill descriptions
flee = Skill("flee")
flee.skilltext = "You attempt to run away from the target.  This may result in returning to the previous encounter."

hide = Skill("hide")
hide.skilltext = "You frantically attempt to hide under the nearest available cover."

flail = Skill("flail")
flail.skilltext = "You attempt to 'fight' in the only way you know how:  battering the subject wildly with both fists"
flail.skilloutcomes = [
        "You hammer your fists wildly at the ",
        "You let loose an anguished cry and flail at the ",
        "You raise your hands above your head in a threatening gesture and flail at the ",
    ]

disgust = Skill("disgust")
disgust.skilltext = "You perform some form of cowardly act involving bodily fluids."

beg = Skill("beg")
beg.skilltext = "You get on your knees and pathetically beg for the target not to harm you."

cower = Skill("cower")
cower.skilltext = ("You attempt to make yourself as non-threatening a target as possible, curling into a ball and cowering in fear.")

nutpunch = Skill("nutpunch")
nutpunch.skilltext = ("You actually attempt to attack the target by punching it in the nuts or other apparently vulnerable area.")

# game encounters
e1 = Encounter(1)
e1.encountertext = f'''
Walking down the path, you see a large gray donkey in the middle of the road.  It doesn't appear to be interested in moving any time soon.
'''

#testing

# while True:
#     print("\n".join(p1.skills))
#     x = input("What do you do? : ")
#     if x in donkey.weaknesses:
#         print(donkey.successtext)
#         break
#     elif x in donkey.resistances:
#         print(donkey.failtext)
#         break
#     else:
#         print("nothing happens")
#         continue

chooseskills()



