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
        self.specialfail = []

def enemyencounter(name):
    while True:
        print("\n".join(p1.skills))
        x = input("What do you do? : ")
        if x in name.weaknesses:
            print(name.successtext)
            break
        elif x in name.resistances:
            print(name.failtext)
            break
        else:
            print("nothing happens")
            continue

#example encounter stats
p1 = Player("Florbert The Unseemly",20)
p1.skills = ["hide","cower","flail"]
donkey = Enemy("donkey")
donkey.successtext = "It looks at you with what appears to be confusion and slowly saunters down the road"
donkey.failtext = "It tramples you.  You die."
donkey.specialfail = "You punch the donkey's balls with all your might.  It makes a startled cry and kicks you in the head. It then runs away from you down the path.  You may proceed, but lose 4 HP"
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
def playername():
    name = input("What is your name? ")
    return name

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

        def outcome(skillname):
            return random.choice(skillname.skilloutcomes)

# skill descriptions
flee = Skill("flee")
flee.skilltext = "You attempt to run away from the target.  This may result in returning to the previous encounter."

hide = Skill("hide")
hide.skilltext = "You frantically attempt to hide under the nearest available cover."
hide.skilloutcomes = "You"

flail = Skill("flail")
flail.skilltext = "You attempt to 'fight' in the only way you know how:  battering the subject wildly with both fists"
flail.skilloutcomes = [
        "You hammer your fists wildly at the ",
        "You let loose an anguished cry and flail at the ",
        "You raise your hands above your head in a threatening gesture and flail at the ",
        "You screech like an enraged child and aggressively thump your balled fists against the #ENEMYNAME#",
        "Making a noise that bears an uncanny resemblance to a broken teakettle, you lash out wildly with your fists."
    ]

disgust = Skill("disgust")
disgust.skilltext = "You perform some form of cowardly act involving bodily fluids."
disgust.skilloutcomes = [
    "Quivering in abject terror at the sight of the #ENEMYNAME#, you void your bowels.",
    "A warm, damp wetness spreads across the front of your pants as your bladder releases.",
    "A fetid, earthy stench surrounds you as you fill your trousers.",
    "You groan weakly as a flood of liquid diarrhea spills down your legs.",
    "Literally sick with fear, you vomit profusely on the feet of the #ENEMYNAME#",
    "You double over and vomit on the ground at the sight of the #ENEMYNAME#"
]

beg = Skill("beg")
beg.skilltext = "You get on your knees and pathetically beg for the target not to harm you."
beg.skilloutcomes = [
    "You prostrate yourself before the #ENEMYNAME# and plead for mercy.",
    "You fall upon your knees sobbing, and beg for your life.",
    "Gibbering like a child, you fall upon the ground and beg the #ENEMYNAME# not to harm you",
    "'Please, please, please don't hurt me!  You sob pathetically."

]

cower = Skill("cower")
cower.skilltext = ("You attempt to make yourself as non-threatening a target as possible, curling into a ball and cowering in fear.")
cower.skilloutcomes = [
    "Quaking in terror, you fall upon the ground into a fetal position.",
    "Visibly trembling, you press your face into your palms and sob profusely.",
    "Shivering with fear and paralyzed with fright, you stand stock still and blubber incoherently.",
    "Wracked with intense tremors, you double over and mumble incoherent nonsense."
]

nutpunch = Skill("nutpunch")
nutpunch.skilltext = ("You actually attempt to attack the target by punching it in the nuts or other apparently vulnerable area.")
nutpunch.skilloutcomes = [
    "You awkwardly cock your fist back and unleash a reckless haymaker",
    "Aiming for the private parts of the #ENEMYNAME#, you swing wildly with your balled fist.",
    "Seeing an opportunity to fight as dirty as possible, you throw a punch aimed at the target's genitals."
]

# game encounters
e2 = Encounter(1)
e2.encountertext = f'''
You wander carefully through the smoking wreckage of your former home.  As you near the outskirts of Florpflump, you are startled by the sounds of a plaintive cry for help.  It appears to be coming from behind a nearby woodpile.

If you choose to investigate, press 1.
If you choose to ignore the noise and continue down the lane leading out of Florpflump, press 2.
'''
x = yourchoice()
if x == 1:
    encounter2()
elif x == 2:
    encounter3()

e2 = Encounter(2)
e2.encountertext = f'''
Creeping closer to the woodpile, you see the battered form of Old Scrapdapple, the village mayor, and your chief tormentor throughout your younger years.  You vividly recall that it was Scrapdapple himself who gave you the moniker {playername}.  He is gravely wounded, and holds out a hastily scrawled note in a charred, bleeding hand.

"Take this, {playername}...  It has vital information that must be passed on... Please...

If you simply take the note and proceed on the path out of the village, press 1.

If you choose to instead mock the mayor's desperate pleas and piss on his dying face before leaving the village, press 2.
'''
while True:
    x = yourchoice()
    if x == 1:
        print("You mumble an awkward thanks and take the note.  A gout of blood pours out of Scrapdapple's mouth as he attempts to smile.  You turn from the grisly sight and proceed down the path leading out of the village.")
    elif x == 2:
        print("Scrapdapple gazes at you with a look of what is initially confusion, and then dawning horror as you unlace your trousers.  He attempts to scream, but his final cries transform into a hideous gargle as you unleash a stream of urine into his bleeding mouth. You make sure that the last sight he sees is you grinding his note into the ground as you walk away.")


e3 = Encounter(3)
e3.encountertext = f'''
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





