import random
suffix = [
    "Cowardly",
    "Wretched",
    "Filthy",
    "Unkempt",
    "Muck-Smeared",
    "Besmirched",
    "Pariah",
    "Unseemly",
    "Off-Putting",
]

name = input("What is your name? ")

introtext = f'''
THE STORY SO FAR

All was well in the village of Florpflump, a peaceful hamlet on the edge of the kingdom of Blurble.  Until one day, out of nowhere, it was attacked by the sworn enemies of Blurble, the Diarrheaservants of Karn.  The brave warriors of Florpflump were slain, along with all of the other villagers...

Except for one.

When the attack came, you were first to hear the hoofbeats of the oncoming Karn forces.  Instead of alerting the villagers, you hid, cowering beneath your bed.

After the final din of battle has faded, you venture out into the smoking ruins of the village.

For years, the villagers had mocked you for your personal habits, hygeine, and behavior.  Now you {name} the {random.choice(suffix)}, who were too afraid of splinters to assist in farming; too socially inept to participate in town meetings, are the sole survivor of the massacre of Florpflump. 

No more will small children throw rocks at you and mock your stench.  No more will townsfolk cross the street when you approach and laugh under their breath.  For you alone can alert the forces of Blurble to the impending threat of the Karn.  

The time has come, {name}.  Let the adventure begin!

'''

print(introtext)