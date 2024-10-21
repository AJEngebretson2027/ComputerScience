# basing this project around my dnd campaign from my prespective of my character
# i was originally going to have you choose between my different party members, but that would be too complitcated
# you are starting after you take a job from cortland to escort a caravan for a week to Carewick

import random

def adv_start():
    print("You start out around a caravan, escorting it to the nearby town of Carewick.")
    print("You are Anthony Spellhardt, a swordsage based aroun the Desert Wind school (fire)")
    print("nothing happens during the day, and for tonight you were choosen to keep watch for a few hours")

    print("You stand guard listening and watching during the night, thankfully you have dark vision which allows you to see during the night")
    spot = print(random.randint(1,20))
    listen = print(random.randint(1,20))

    print("you rolled " + str(spot + 3) + " for spot")          # in 3.5e perception does not exist, instead being either spot, listen, or search
    print("you rolled " + str(listen + 1) + " for listen")      # you can have different skill modifiers, based on the ability mod, rank, misc changes, and armor check penalties (ACP)

    if spot >= 14:
        print("As you are looking around, you spot a wolf watching you intently")
        spot_wolf

    elif listen >= 14:
        print()
        hear_something

    elif spot >= 14 and listen >= 14:
        print("as you are looking around you hear something move, you look towards the sound and spot a wolf")