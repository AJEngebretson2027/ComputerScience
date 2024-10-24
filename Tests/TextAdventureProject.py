# basing this project around my dnd campaign from my prespective of my character
# i was originally going to have you choose between my different party members, but that would be too complitcated
# you are starting after you take a job from cortland to escort a caravan for a week to Carewick

health = 10
ac = 17     #ac stands for armor class, it is how high the enemy has to roll to hit you. you can increase this through armor, class skills, or some feats
exp = 0

import random

def adv_start():
    print("You start out around a caravan, escorting it to the nearby town of Carewick.")
    print("You are Anthony Spellhardt, a swordsage wielding a halberd and based aroun the Desert Wind school (fire)")
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
    print("You are both staring at each other. What you you do?")       #different options you can choose, may lead to weaker or stronger encounters
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
                attack_wolf

            elif AoO == 2:
                print("the wolf runs off.")
                wolf_ambush

    if choice == 2:
        print("as you start to move up to attack the wolf, it runs off before you can hit it.")
        wolf_ambush


    if choice == 3:
        print("you bend down and hold out your hand, allowing it to sniff it. it sniffs a bit before running off")
        wolf_ambush

def attack_wolf():
    attack_AoO = (random.randint(1,20))
    print ("you rolled " + str(attack_AoO + 6) + "for attack")

    if attack_AoO >= 14:
            damage_AoO = (random.randint(1,10))
            print("you hit the wolf and deal " + str(damage_AoO + 4) + "points of damage")      #im just now realizing how many nested if statements i need for this
            if damage_AoO == 14:
                print("you kill the wolf before it can return to its pack.")
                wolf_ambush

            else:
                print("you injure the wolf, but it manages to escape.")
                wolf_ambush
    elif attack_AoO < 13:
                    print ("you miss the wolf as it runs away, back to its pack")
                    wolf_ambush

def hear_something():
     print("What would you like to do?")
     print("1. investigate the noise")
     print("2. ignore the noise, must've been the wind")    #skyrim reference

     heard_something = input(">")
     heard_something = int(heard_something)
     if heard_something == 1:
          print("you walk over to where you saw the noise, and you see a wolf.")
          spot_wolf
     elif heard_something == 2:
          print("you decided it is nothing, continuing your watch.")
          wolf_ambush

def wolf_ambush():
     print("You continue on with your night, and eventually switchng places with ashmook, the party's monk.")
     print("but before you can even take off your armor, you hear howling of wolfs behind your camp")
     print("you quickly get out your tent, as you see 5 wolfs readying their attack")
     print("you react fast, what do you do?")
     print("1. charge the first wolf you see")
     print("2. move up and yell to attract the wolfs")
     choice2 = input(">")
     choice2 = int(choice2)
     if choice2 == 1:
          attack_wolf2
        
     elif choice2 == 2:
          attract_wolfs

def attack_wolf2():
    print("you cast burning blade before striking the wolf")
    charge_wolf = (random.randint(1,20))
    print("you rolled " + str(charge_wolf + 8) + " for your attack")

    if charge_wolf >= 14:
         print("you manage to hit the wolf")
         charge_damage = (random.randint(1,10))
         bb_damage = (random.randint(1,6))
         total_charge = charge_damage + bb_damage

         print("you hit the wolf, dealing " + str(total_charge + 4) + " damage")
         if total_charge >= 14:
              print("you instantly split the wolf in half, killing it")
              party_wolf
         elif total_charge < 13:
              print("you gravely injure the wolf, but it is still standing")
              party_wolf
    elif charge_wolf < 13:
         print("you strike at the wolf, but it dodges before you hit it.")
         party_wolf

def attract_wolfs():
     print("you move up close to all the wolfs and you yell to get their attention")
     print("three wolfs turn their head, seeing someone seperated from the group they take the opportunity to attack.")
     wolf_attack1 = (random.randint(1,20))
     wolf_attack2 = (random.randint(1,20))
     wolf_attack3 = (random.randint(1,20))
     global health
     
     if wolf_attack1 >= ac:
          wolf_damage1 = (random.randint(1,6))
          print("the wolf bites you in the arm, dealing " + str(wolf_damage1 + 1) + " damage")
          health = health - wolf_damage1
     elif wolf_attack1 < ac:
          print("the wolf attempts to bite you, but you dodge out the way before the bite can land")
    
     if wolf_attack2 >= ac:
          wolf_damage2 = (random.randint(1,6))
          print("the wolf bites you in the leg, dealing " + str(wolf_damage2 + 1) + " damage")
          health = health - wolf_damage2
     elif wolf_attack2 < ac:
          print("you use the shaft of the halberd to deflect a wolfs bite")

     if wolf_attack3 >= ac:
          wolf_damage3 = (random.randint(1,6))
          print("the wolf bites you in the arm, dealing " + str(wolf_damage3 + 1) + " damage")
          health = health - wolf_damage3
     elif wolf_attack3 < ac:
          print("you dodge out the way of the last attack")

     party_wolf

def party_wolf():
     print("your party members move in, killing three of them while your fighter, sherrif, is grappling a wolf")    #sherrif is spelled incorrectly on purpose
     print("sherrif knocks out the wolf, as you manage to kill the last one before it can bite you")                #we actually did this and named him par'ner
     print(" you gain 250 exp")
     global exp
     exp = exp + 250
     print("what do you do now?")
     print("1. go back to sleep")
     print("2. watch as the party attempts to tame the wolf")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          print("you are to tired for their shenanigans, you head back into your tent to take off your armor and head to sleep")
          next_day
     
     elif choice == 2:
        print("you decide to stay for a bit a before heading to sleep")
