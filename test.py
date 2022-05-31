
####
# BLOOD AND TREMBLING
# a text-based RPG adventure
# Text by Jay Brainless 
# Code written by JayO Brainless with assistance from T. Dierking
#Copyright 2022
####
import random
import os
from re import X
from texts import suffix
from time import sleep

#because f strings don't like backslashes
newline = '\n'
#player / enemy stats
class Player:
    def __init__(self,name,hp):
        self.name = name
        self._gold = 0
        self._hp = 20
    
    @property
    def hp(self):
       return self._hp

    @hp.setter
    def hpset(self, value):
       self._hp = value

    @property
    def gold(self):
       return self._gold

    @gold.setter
    def goldset(self, value):
       self._gold = value

    def getgold(self):
        return self.gold

    def setgold(self, newgold):
        self.gold = newgold

    def equipment(self):
        return self.equipment

    def equipment(self, newequip):
        self.equipment = newequip

    def getskills(self):
        text = ", ".join(self.skills)
        return text

class Enemy:
    def __init__(self,name):
        self.name = name
        self.resistances = []
        self.weaknesses = []
        self.successtext = []
        self.failtext = []
        self.failskill = []
        self.specialfail = []
        
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
def name():
    x = input("What is your name? ")
    return x

def playername():
    return f'{name()} the {random.choice(suffix)}'
p1 = Player(playername,20)
p1.skills = ["hide","cower","flail","nutpunch"]
###REPLACE PREDEFINIED SKILLS WITH SKILLCHOICE BELOW

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


#ENCOUNTER LOGIC - NEED TO GET THS WORKING BEFORE FINIISHINIG STORY
class Encounter:
    def __init__(self,encounternum):
        self.encounternum = encounternum
        self.encountertext = ""
        # self.choices = []
        self.skillchoices = p1.getskills()
        
    @property
    def choices(self):
        choice = int(input("Your choice?: "))
        self.choices[choice]
    
    # def use_skill(self, skillname):
    #     self.use_skill = self.skillname
    #     self.skillname = Skill.skillname
    #     text = None
    #     if skillname in Enemy.weaknesses:
    #         text = self.successtext
    #     elif skillname in Enemy.weaknesses:
    #         text = self.failtext
    #     else:
    #         text = skillname.nope()  
    def combat_encounter(self,enemy):
        print(self.encountertext)
        print(f'Your Skills: {self.skillchoices}{newline}')
        answer = input("Which skill do you wish to use? ")
        for skill in p1.skills:
            if skill.skillname == answer:
                skill.useon(enemy)
                break
            else:
                print("You do not possess that skill!")

#SKILL LOGIC
class Skill:
    def __init__(self,skillname):
        self.skillname = skillname
        self.skilltext = " "
        self.skilloutcomes = []
        self.noeffects = []

    def use(self,enemy):
        self.enemy = enemy
        text = random.choice(self.skilloutcomes)
        return text
    
    def useon(self,enemy):
        print(f'{self.use(enemy)}{newline}')
        sleep(3)
        text = None
        if self.skillname in enemy.weaknesses:
            text = enemy.successtext
        elif self.skillname in enemy.resistances:
            text = enemy.failtext
        elif self.skillname in enemy.specialfail:
            text = enemy.specialfail
        else:
            text = self.noeffects
        return text
        
    def nope(self):
        return random.choice(self.noeffect)

# SKILL DESCRIPTIONS
flee = Skill("flee")
flee.skilltext = "You attempt to run away from the target.  This may result in returning to the previous encounter."

hide = Skill("hide")
hide.skilltext = "You frantically attempt to hide under the nearest available cover."
hide.skilloutcomes = [
    "Like a small rodent, you desperately attempt to scurry under the nearest available cover.",
    "Your eyes widen with terror and you scramble for a suitable place to hide.",
    "In a panicked attempt to conceal yourself, you dive under the nearest available hiding place.",
]
hide.noeffects = [

]

flail = Skill("flail")
flail.skilltext = "You attempt to 'fight' in the only way you know how:  battering the subject wildly with both fists"
flail.skilloutcomes = [
        "You hammer your fists wildly at the ",
        "You let loose an anguished cry and flail at the ",
        "You raise your hands above your head in a threatening gesture and flail at the ",
        "You screech like an enraged child and aggressively thump your balled fists against the {enemy.name}",
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
    "You double over and vomit on the ground at the sight of the #ENEMYNAME#",
    "A sound like tearing paper fills the air as you are wracked with several violent sharts.  Shortly thereafter, a tremendous explosion of watery feces fills your pants."
]
disgust.noeffects = "The putrid stench of your own bodily fluids surrounds you, but the enemy.name simply stares at you with incomprehension."
beg = Skill("beg")
beg.skilltext = "You get on your knees and pathetically beg for the target not to harm you."
beg.skilloutcomes = [
    "You prostrate yourself before the #ENEMYNAME# and plead for mercy.",
    "You fall upon your knees sobbing, and beg for your life.",
    "Gibbering like a child, you fall upon the ground and beg the #ENEMYNAME#  not to harm you",
    "'Please, please, please don't hurt me!  You sob pathetically.",

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
    "Aiming for the private parts of the , you swing wildly with your balled fist.",
    "Seeing an opportunity to fight as dirty as possible, you throw a punch aimed at the target's genitals."
]

# GAME ENCOUNTERS
e1 = Encounter(1)
e1.encountertext = f'''
You wander carefully through the smoking wreckage of your former home.  As you near the outskirts of Florpflump, you are startled by the sounds of a plaintive cry for help.  It appears to be coming from behind a nearby woodpile.


If you choose to investigate, press 1.

If you choose to ignore the noise and continue down the lane leading out of Florpflump, press 2.
'''

e2 = Encounter(2)
e2.encountertext = f'''
Creeping closer to the woodpile, you see the battered form of Old Scrapdapple, the village mayor, and your chief tormentor throughout your younger years.  You vividly recall that it was Scrapdapple himself who gave you the moniker {playername}.  He is gravely wounded, and holds out a hastily scrawled note in a charred, bleeding hand.

"Take this, {name}...  It has vital information that must be passed on... Please...

If you simply take the note and proceed on the path out of the village, press 1.

If you choose to instead mock the mayor's desperate pleas and piss on his dying face before leaving the village, press 2.
'''
e2.choice1 = "You mumble an awkward thanks and take the note.  A gout of blood pours out of Scrapdapple's mouth as he attempts to smile.  You turn from the grisly sight and proceed down the path leading out of the village."

e2.choice2 = "Scrapdapple gazes at you with a look of what is initially confusion, and then dawning horror as you unlace your trousers.  He attempts to scream, but his final cries transform into a hideous gargle as you unleash a stream of urine into his bleeding mouth. You make sure that the last sight he sees is you grinding his note into the ground as you walk away."

e3 = Encounter(3)
e3.encountertext = f'''
Walking down the path, you see a large gray donkey in the middle of the road.  It doesn't appear to be interested in moving any time soon.
'''

# e4 = Encounter(4)
# def notecheck():
#     if "crumpled note" in p1.equipment:
#         additionaltext = 'As you ponder which way to go, you remember the note that Scrapdapple gave you.  Although nearly illegible, you manage to make out the words, "treasure" and "grove"'
#         return additionaltext
#     else:
#         pass
# e4.encountertext = f'''
# With the donkey out of the way, you continue to walk down the path.  After some time, you come to a crossroads.  The westward path looks to lead toward a large grove of trees far in the distance.  The Eastward path winds around a large hill.

# {notecheck()}

# If you take the westward path towards the grove, press 1
# If you take the Eastward path toward the hill, press 2
# If you choose to continue north, press 3
# '''

# e5 = Encounter(5)
# e5.encountertext = f'''
# You head westward towards the trees.  The hot afternoon sun beats down upon you as you trod the dusty path into the grove.  Welcoming the shade offered by the trees, you pause and rest upon a nearby log.  Suddenly, you hear a crashing noise behind you, and you turn to find yourself face to face with a large group of Ogres!  They stare at you with wicked amusement as drool drips slowly from their enormous, fanged mouths.

# 'Well, well, well...  Wot 'ave we 'ere?  One of the Ogres says menacingly.  'a lil' lost lamb all alone in the forest?  It's been a long time since we 'ad lamb for supper!  

# They begin to move slowly toward you, brandishing long, jagged knives.
# '''
# def finaljoke():
#     if "crumpled note" in p1.equipment:
#         additionaltext = 'You realize, too late, that Scrapdapple has played one final, cruel joke upon you, and that he must have written the note as he saw you approaching.  There is no treasure here, only your certain doom.'
#         return additionaltext
#     else:
#         pass
# ogre = Enemy("ogre")
# ogre.resistances = ["cower","hide","flee","nutpunch","flail","beg"]
# ogre.weaknesses = ["disgust"]

# if e5.use_skill(cower):
#     ogre.failtext = f'''
#     {cower.outcome} 

#     {finaljoke()} The last thing you hear is the Ogres laughing at your cowardice as they hack you to pieces'''
# elif hide.use_skill:
#     ogre.failtext = f'''
#     {hide.outcome} 

#     {finaljoke()} Your attempts to hide, however, are futile.  You have survived the massacre of your home only to end up in an Ogre's stewpot.'''
# elif flee.use_skill:
#     ogre.failtext = f'''
#     {flee.outcome} 

#     {finaljoke()} You manage to duck between the legs of one of the Ogres and desperately run toward the edge of the grove, only to feel a hot flash of pain as long, thick claws dig mercilessly into your back.'''
# elif nutpunch.use_skill:
#     ogre.failtext = f'''
#     {nutpunch.outcome} 

#     {finaljoke()} The ogres look at you with amusement as your blow goes wide.  The grove rings with their hideous laughter.
#     'Oooh, This'un 'ere's a fiesty one!' One of the Ogres cackles.  'This will be some spicy stew!'

#     '''
# elif disgust.use_skill:
#     ogre.successtext = f'''
#     {finaljoke()}

#     {disgust.outcome}

#     The Ogres look upon you with disgust and horror.  'Ewwww, this'un's messed 'imself!  The head Ogre shouts.  'By Grokflarp's ragged teats, the smell is awful!  We'll never be able to clean 'im up!  Let's get out of 'ere!

#     You breathe a sigh of relief, barely noticing the stench of your own filth as the Ogres tromp away deeper into the woods.
#     '''


#example encounter stats
# p1 = Player("Florbert The Unseemly",20)

e6 = Encounter(6)
e6.encountertext = '''
You make your way down the path towards the hill, you notice a figure in the distance, apparently walking the same direction you are going. As you approach the foot of the hill, you realize it is and old beggar-man with a large knapsack.  He holds a hand out and asks,

'Hello, fellow traveler, care to spare a penny for an old man?'
'''
###
# flail or nutpunch - "The old beggar stumbles back with a startled look and falls flat on his back.  You proceed, confident that you have vanquished what was certainly a dangerous foe."

# hide / cower / disgust - "The old man looks at you with puzzlement and then chuckles heartily.  'umm, here, take this, looks like you need it more than me."

# flee - 'you run screaming from the sight of the old beggar man.'


### TEST ENCOUNTER STATS

donkey = Enemy("donkey")
donkey.failskill = nutpunch
donkey.successtext = "The donkey looks at you with what appears to be confusion and slowly saunters down the road"
donkey.failtext = "It tramples you.  You die."
donkey.specialfail = "You punch the donkey's balls with all your might.  It makes a startled cry and kicks you in the head. It then runs away from you down the path.  You may proceed, but lose 4 HP"
donkey.resistances = "cower"
donkey.weaknesses = "flail"

#######

#TESTING AREA
print(nutpunch.useon(donkey))
