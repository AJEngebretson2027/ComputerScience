# basing this project around my dnd campaign from my prespective of my character
# i was originally going to have you choose between my different party members, but that would be too complitcated
# you are starting after you take a job from cortland to escort a caravan for a week to Carewick

health = 10
ac = 17     #ac stands for armor class, it is how high the enemy has to roll to hit you. you can increase this through armor, class skills, or some feats
exp = 0
level = 1

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

    if spot + 3 >= 14:
        print("As you are looking around, you spot a wolf watching you intently.") 
        spot_wolf

    elif listen + 1 >= 14:
        print("You hear a sound from the brush around 20 feet away.")
        hear_something      #this will ultimately lead to spot_wolf

    elif spot + 3 >= 14 and listen + 1 >= 14:       #if you are good at gambling lol
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

    if attack_AoO + 6 >= 14:
            damage_AoO = (random.randint(1,10))
            print("you hit the wolf and deal " + str(damage_AoO + 4) + "points of damage")      #im just now realizing how many nested if statements i need for this
            if damage_AoO + 4 == 14:
                print("you kill the wolf before it can return to its pack.")
                wolf_ambush

            else:
                print("you injure the wolf, but it manages to escape.")
                wolf_ambush
    elif attack_AoO + 6 < 13:
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

    if charge_wolf + 8 >= 14:
         print("you manage to hit the wolf")
         charge_damage = (random.randint(1,10))
         bb_damage = (random.randint(1,6))
         total_charge = charge_damage + bb_damage

         print("you hit the wolf, dealing " + str(total_charge + 5) + " damage")
         if total_charge + 5 >= 14:
              print("you instantly split the wolf in half, killing it")
              party_wolf
         elif total_charge + 5 < 13:
              print("you gravely injure the wolf, but it is still standing")
              party_wolf
    elif charge_wolf + 8 < 13:
         print("you strike at the wolf, but it dodges before you hit it.")
         party_wolf

def attract_wolfs():
     print("you move up close to all the wolfs and you yell to get their attention")
     print("three wolfs turn their head, seeing someone seperated from the group they take the opportunity to attack.")
     wolf_attack1 = (random.randint(1,20))
     wolf_attack2 = (random.randint(1,20))
     wolf_attack3 = (random.randint(1,20))
     global health
     
     if wolf_attack1 + 3 >= ac:
          wolf_damage1 = (random.randint(1,6))
          print("the wolf bites you in the arm, dealing " + str(wolf_damage1 + 1) + " damage")
          health = health - wolf_damage1 + 1
     elif wolf_attack1 < ac:
          print("the wolf attempts to bite you, but you dodge out the way before the bite can land")
    
     if wolf_attack2 + 3 >= ac:
          wolf_damage2 = (random.randint(1,6))
          print("the wolf bites you in the leg, dealing " + str(wolf_damage2 + 1) + " damage")
          health = health - wolf_damage2 + 1
     elif wolf_attack2 < ac:
          print("you use the shaft of the halberd to deflect a wolfs bite")

     if wolf_attack3 + 3 >= ac:
          wolf_damage3 = (random.randint(1,6))
          print("the wolf bites you in the arm, dealing " + str(wolf_damage3 + 1) + " damage")
          health = health - wolf_damage3 + 1
     elif wolf_attack3 < ac:
          print("you dodge out the way of the last attack")
     
     if health < 0:
          knocked_out
     elif health >= 0:
          party_wolf
     elif health <= -10:      #this is a possiblity, as you need to get to -10 hp to fully die, or you get knocked out, and if all 3 wolfs hit max damage, they deal 21 damage
          death

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
        print("ashmook attempts to feed it some meat, which the wolf didnt run but was still wary of us")
        print("You start healing everyone who took damage, bandaging everyone who took damage")
        print("Grey bane tried to heal you but failed, but ashmook successfully managed to heal you which everyone tried to heal you as well")        #this happened and everyone but ashmook rolled low
        print("you head back in your tent and head to sleep")
        next_day

def next_day():
     global health
     health = health + 2
     if health >= 10:
          health = 10
     print("you wake up the next day, getting dressed and feeling a bit better then last night")         # resting restores your level worth of hp, but if you were healed then you would heal double your level
     print(" you pack up your tent and put it in the back of the caravan. continuing back on the road")
     print("only one eventful thing happened while walking, you noticed a small humanoid watching you, pretty deep into the tree line with a wolf at their side")
     print("what do you do?")
     print("1. call out to them")
     print("2. attempt to reach them")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          print("you call out to them, but all they do is get on the wolf and ride away")
          print("you know the wolf is too fast for you to catch up so you continue on your way")
          day_night
     elif choice == 2:
          print("you head into the brush, getting to about halfway to them before the person gets on the wolf and rides off")
          day_night

def day_night():         # destroyed campsite
     print("other then the humanoid watching you, nothing else happens")
     print("your party finds a good resting place and sets up camp for the night, on your watch, nothing happens and the night passes uneventfully")
     print("its the next day and you head back on the road, eventually getting to a turn in the road, where you can see a caravan flipped, with dead people and horses")
     print(" it seemed like things were ransacked from the caravan, and only the clothes remained on the bodies")
     print("there seems to be a dirt trail coming from the main path, what do you do?")
     print("1. look around to see what happened")
     print("2. head down the dirt trail")
     print("3. keep heading down the path, this doesn't concern us")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          investigation
     elif choice == 2:
          dirt_trail
     elif choice == 3:
          print("you decide to stay in the back of the caravan as you remember cortland left a box of books that cortland left open")
          print("one book catches your eye, Beware! Kygel's Keep. You open it up and start reading")
          print("Kygel's Keep was a castle that is right next to Carewick. Its lord mysteriously dissapeared and it was left in disrepair. it is said that a evil green dragon named kygel moved in below the castle. it is inhabited by Kobolds and mostly keep to themselves")
          print("your party members return from a cave you didnt see and it seems like reef took some fall damage as you were informed there was a pitfall trap.")
          print("you all decide that its best to keep going")
          the_bridge

def investigation():
     print("you look at the bodies, and you see claw marks, but its too big to be a wolfs claw")
     print("heading over to a tent, seeing large claw marks in the cloth and a body sticking out from the tent.")
     print("you see a cave just down the trail, there is a sign next to with a skull engraved into the wood, as you get closer you see a sign inside saying to keep out")
     print("do you enter?")
     print("1. yes")
     print("2. no")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          cave
     elif choice == 2:
          print("you decide to stay behind, watching the caravan while everyone else goes inside")

def the_bridge():
     print("after a bit you make it to a medium sized bridge, and before you cross, the person watching you reappears")
     print("")

def dirt_trail():
     print ("you walk along the dirt trail and at the end of it there is a cave. there is a sign at the entrance with a skull engraved into it")
     print("as you get closer you see a sign saying to keep out")
     print("do you enter?")
     print("1. yes")
     print("2. no")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          cave
     elif choice == 2:
          print("you decide that its best to not to go into the cave, staying behind to protect the caravan")
          the_bridge

def cave():
     print("you carfully head into the cave, when you get the to sign you see that the cave goes to the left and the right")
     print("to the left you see a barricade blocking your way, and to the right is another turn")
     print("what do you do?")
     print("1. head to the right")
     print("2. break down the barricade")
     print("3. lets head back, this isnt worth it")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          print("you walk deeper into the cave and you turn right again, seeing a body and a activated trap")
          deeper_cave
     elif choice == 2:
          print("you aren't as strong as the other party members so you stand guard as they break it down")
          break_bar
     elif choice == 3:
          print("you think this is too sketchy and you decide to head back")
          the_bridge

def deeper_cave():
     print("you walk past the body, moving silently")
     print("there is a wider area and a door at the back right of the opening")
     print("what do you do?")
     print("1. head through the middle")
     print("2. stick to the right wall")
     print("3. stick to the left wall")
     print("4. this is getting riskier, we should head back")
     choice = input(">")
     choice = int(choice)
     if choice == 1:
          print("as you are walking, you feel the ground give out, act fast or fall")
          print("because of your race, you have a devils favor which will increase your reflex by +2. do you use it?")
          print("1. yes")
          print("2. no")
          devils_favor = input(">")
          devils_favor = int(devils_favor)
          if devils_favor == 1:
               reflex_devil = (random.randint(1,20))
               print("you rolled " + str(reflex_devil + 7) + " for reflex")
               if reflex_devil + 7 >= 20:
                    print("you just barely jump out the way, as a 15 foot hole opens up before you")
                    print("knowing there are dangerous traps, you head back")
                    the_bridge
               elif reflex_devil + 7 < 20:
                    fall1 = (random.randint(1,6))
                    fall2 = (random.randint(1,6))
                    total_fall = fall1 + fall2
                    print("you fall in, falling hard on your back, taking " + str(total_fall) + " damage")
                    global health
                    if health - total_fall >= 1:
                         print("you live, but you are hurting.")
                         print("one of your party members throws down a rope, you grab on and climb back up deciding to head back")
                         the_bridge
                    
                    elif health - total_fall < 0:
                         print("you are knocked unconscious")
                         knocked_out



