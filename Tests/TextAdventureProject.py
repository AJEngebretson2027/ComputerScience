# basing this project around my dnd campaign from my prespective of my character
# i was originally going to have you choose between my different party members, but that would be too complitcated
# you are starting after you take a job from cortland to escort a caravan for a week to Carewick

import random

def adv_start():
    print("You start out around a caravan, escorting it to the nearby town of Carewick.")
    print("You are Anthony Spellhardt, a swordsage based aroun the Desert Wind school (fire)")
    print("nothing happens during the day, and for tonight you were choosen to keep watch for a few hours")

    print("You stand guard listening and watching during the night, thankfully you have dark vision which allows you to see during the night, although limited")
    spot = (random.randint(1,20))
    listen = (random.randint(1,20))

    print("you rolled " + str(spot + 3) + " for spot")          # in 3.5e perception does not exist, instead being either spot, listen, or search
    print("you rolled " + str(listen + 1) + " for listen")      # you can have different skill modifiers, based on the ability mod, rank, misc changes, and armor check penalties (ACP)

    if spot >= 14:
        print("As you are looking around, you spot a wolf watching you intently.") 
        spot_wolf

    elif listen >= 14:
        print("You hear a sound from the brush around 20 feet away.")
        hear_something      #this will ultimately lead to spot_wolf

    elif spot >= 14 and listen >= 14:       #if you are good at gambling lol
        print("As you are looking around you hear something move, you look towards the sound and spot a wolf.")
        spot_wolf       

    else:
        print("You spot nothing out of the ordinary")
        wolf_ambush
    
def spot_wolf():
    print("You are both staring at each other. What you you do?")
    print("1. Scare off the wolf by yelling")
    print("2. attempt to attack the wolf")
    print("3 try to befriend the wolf")

    choice = input(">")
    choice = int(choice)

    if choice == 1:
        intimidate = (random.randint(1,20))
        print ("you rolled " + str(intimidate) + " for intimidate.")
        if intimidate >= 14:
            print ("the wolf is startled and begins to run away from you, allowing you to get an Attack of Opportunity")        #attack of opportunitys (AoO) are a mechanic where if a enemy is running away from you or are moving through squares you are adjacent to more than once you get a free attack
            print ("Do you take the attack of Opportunity? (this action may have consquences)")
            print ("1. Yes\n2. No")
            AoO = input(">")
            AoO = int(AoO)
            if AoO == 1:
                attack_AoO = (random.randint(1,20))
                print ("you rolled " + str(attack_AoO + 6) + "for attack")
                if attack_AoO >= 14:
                    damage_AoO = (random.randint(1,10))
                    print("you hit the wolf and deal " + str(damage_AoO + 4) + "points of damage")      #im just now realizing how many nested if statements i need for this
                    if damage_AoO == 14:
                        print("you kill the wolf before it can return to its pack.")
                    else:
                        print("you injure the wolf, but it manages to escape.")
                elif attack_AoO < 13:
                    print ("you miss the wolf as it runs away, back to its pack")
                    str_wolf_ambush

            elif AoO == 2:
                print("the wolf runs off.")
                wolf_ambush
    if choice == 2:
        print("as you start to move up to attack the wolf, it runs off before you can hit it.")
        wolf_ambush

    if choice == 3:
        print("you bend down and hold out your hand, allowing it to sniff it. it sniffs a bit before running off")
        weak_wolf_ambush
    

