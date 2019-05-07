#Python Adventure Game

import random
import sys
import os
import time




screen_width=100

#Player Set-up

class player:

    """The class is the player 
    
    Define function to initialize the player

    Includes:
    self.name= inputted name string
    self.race=inputted race from suggested list
    self.hp= designated hp based on race
    self.inventory= items gathered during game as a dictionary
    """

    def __init__(self):
        self.name = ''
        self.race=[]
        self.hp = 0
        self.inventory = {}


### MAP of game

""""

                         ________  
                        |        |
                        | Dining |
                        |  Room  |
                        |        |  
|--------------------------------|
|Den   Hallway                   |
|                                |
|         ______________________ |
|         |               |       |   
|Front    |               |       |
| Entrance|               | Parlor|
|_________|               |       |
                          |_______|                        


"""

"""Defines answers for player inputs"""
answer_A =["A", "a"]
answer_B =["B", "b"]
answer_C = ["C", "c"]
answer_D=["D","d"]
answer_E=["E", "e"]
answer_F=["CHECK INVENTORY", "check inventory"]

myplayer=player()
"""Defines myplayer to function player which is initializer"""
playerhealth=15
"""Sets players health at 15"""
playerattack=random.randint(1,20)
"""Sets player's attack damage at random integer between 1-20"""
monsterhp=20
""""Sets monster's health at 20"""
monsterattack=random.randint(1,5)
"""Sets monster's attack damage at random integer between 1-5"""

inventory={'sword': 'This is a nice looking sword! I could kill something with this'}
"""Initial inventory which only includes sword"""

answer_puzzle=["LOOK BEHIND RED PILLOW", "look behind red pillow", "Look Behind Red Pillow"]
"""Sets viable answers for puzzle"""

def check_inventory():
    print(inventory)

def hallway():
    """Defined by health of monster and player
    Parameters:
     arg1 (int): Monster and player are still alive (have health above 0)
     Returns:
         int: Attack option continues; prints health of player and monster; requires input of next choice by player

         parameters:
         arg1.5 (int): Attack
         returns:
            int: Subtracts damage from health and decision depends on health
          arg1.6 (int): Run
          returns:
            int: prints run function

      arg2 (int): Monster and player are dead (both have health at or below 0)
      Returns:
          int: prints death function (game ends)

      arg3(int): Monster is alive but player is dead (health below 0)
      Returns:
          int: prints death function (game ends)

      arg4(int): Monster is dead and player is alive (health above 0)
      Returns
        int: prints text and continues game
        """
    if monsterhp>0 and playerhealth>0:
                print("You attack the beast and draw back . The creature lunges forward. Both of you performing the dance of enemies.\n"
                      "Your health is", playerhealth, "/15.\n"
                      "The monsters health is", monsterhp, "/20\n")
                print("What do you want to do?\n"
                      "A. Attack\n"
                      "B. Run Away\n")
                choice = input(">")
                if choice in answer_A:
                    attack()
                elif choice in answer_B:
                    option_run()
    elif monsterhp <= 0 and playerhealth <= 0:
        death()
    elif monsterhp > 0 and playerhealth <= 0:
        print(" You fall to the ground trying to crawl away from the monster. It only gets bigger and proceeds to form an orfice to engulf you.")
        death()
    elif monsterhp <= 0 and playerhealth > 0:
        print("The monster is dead. It falls from its form and splashes into liquid on the floor. You heave a great sigh of relief\n")
        print("You continue on your journey to escape from the castle.\n")
        cross_roads()

def attack():
    """Defines attack function
    Health, attack, and hp are defined as global variables
    which can be used anywhere in the program

    Player health is reduced by monster attack
    monsterhp is reduced by player attack

    prints hallway function
    """
    global playerhealth
    global playerattack
    global monsterhp
    global  monsterattack
    playerhealth=playerhealth-monsterattack
    monsterhp=monsterhp-playerattack
    hallway()

###ONLY 3 POSSIBLE ENDINGS (GOOD, BAD, AND DEATH)
###MONSTER MUST BE ALIVE BY END OF GAME TO WIN

def bad_end():
    """
    Parameters:
    arg1 (int): Monster is dead but must collect all items (grocery list in den, snout in dining room,
    nail/bowl in parlor, and ask monster for tomato)
    return:
     int: prints bad end and ends the game

    """
    print("You continue around the castle. Searching, collecting, and solving puzzles.\n"
          "However, once you finished, you realized that the monster you were meant to help is dead.\n")
    print("You pass your remaining days by reading until you eventually die of starvation.\n"
         "****BAD END****\n"
         "Please try again")
    sys.exit()


def good_end():
    """
    Parameters:
    arg1 (int): Monster is alive and plaer collected all items (grocery list in den, snout in dining room,
    nail/bowl in parlor, and ask monster for tomato)
    return:
     int: prints good end and ends game
    """
    print("You place the bowl on the ground\n"
          "You grasp the tomato and squeeze it tighlty\n"
          "The juices squirt from in between your fingers into the bowl some on the floor\n"
          "You stop sqeezing and begin kneading the tomato into a pulp\n")
    print("You place the pig snout in the bowl.\n"
          "You bring the nail out and prick your finger. You count the drops into the bowl. 1,2,3\n"
          "You awkwardly present the bowl to the monster who opens up an orfice for you to pour the contents in to.\n"
          "After you pour the contents, a few seconds go by. Soon enough, you hear a low sizzling like frying meat, the dark hallway begins to fill with smoke\n"
          "After the smoke clears, the monster is gone. A key is on the floor.\n"
          "You give a shrug, take the key, and walk to the front entrance\n."
          "You escaped successfully\n"
          "***GOOD END***\n")
    sys.exit()



def death():
    """
    Parameters:
    arg1(int): monster and player are dead (health at or below 0) or just player is dead
        return:
        int: prints death and ends game
    """
    print("Gasping for your last breath, your eyes search for anything before death takes you.\n"
          "You fall into darkness.\n")
    print("You died. Please play again ")
    sys.exit()



def option_run():
    """
    Parameters:
    arg1(int): player inputs run as a option to conflict with monster
        return:
        int: prints run text and ends game (you died)
    """
    print("Where do you think you are going?\n"
          "The voice doesnot sound angry but frustrated.\n"
          "You pay no mind and run in the direction the monster isn't. 'I just want to get the hell out of here!' You think on the verge of tears.\n"
          "You hear a squelching sound behind you. Darkness engulfs you. It seems like the monster has eaten you.\n ")
    print("***DEAD END***\n"
          "Please try again!\n")
    sys.exit()

###Title Screen ###

def title_screen_selections():

    """Brings up option to allow play, help, and quit function
    Parameters:
    arg 1 (int): play

    Returns:
    int: Starts game

    arg 2 (int): help

    Returns:
    int: brings up helpful tips

    arg 3 (int): quit
    int: ends game

    arg 4 (int): invalid command
    int: prompts player to input a valid command and starts process over

    """
    option= input("> ")
    if option.lower()==("play"):
        setup_game()
    elif  option.lower()== ("help"):
        help_menu()
    elif option.lower()==("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Command not valid. Please Enter play, help, or quit")
        option=input("> ")
        if option.lower() == ("play"):
            setup_game()  
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

###Title screen selections ###

def title_screen():
    """Prints the title screen"""
    os.system('clear')
    print('Welcome to Phadalin!')
    print( '    >play    ')
    print('     >help    ')
    print('     >quit    ')
    title_screen_selections()

def help_menu():
    """Prints helpful tips for smooth game play"""
    print(" >Carefully read each section. Your decisions will influence the story.")
    print(' >Type your choices (A,B,C, D, E)')
    print(" >Keep answers to all capital letters or all lower case letters")
    print(" >Type check inventory if you want to check your inventory")
    title_screen_selections()

def setup_game():
    """Starts game"""
    os.system('clear')

##Player name input##
    question_one= 'What do you want your name to be?\n'
    """Prints the name question """
    for character in question_one:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    """Prints selection character by character at 0.05 seconds per character"""
    player_name= input(">")
    """Prompts player to input name"""
    myplayer.name=player_name
    """Inputted name is now class player name"""

##Choosing Race ##
    question_two='What race are you?\n'
    question_twoadd="(You can play as a human, elf or dwarf)\n"
    """Prints the race question"""
    for character in question_two:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question_twoadd:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    """Prints selection character by character at 0.05 seconds per character"""
    player_race= input(">")
    """Prompts player to input race"""
    valid_race=['human', 'elf', 'dwarf']
    """Defines valid races for player to choice from"""
    """If player inputs valid race, print intro and begin game"""
    if player_race.lower() in valid_race:
        myplayer.race=player_race
        print("You are a " + player_race + ".\n")
        question_three= 'Hello '+ player_name+ '!\n'
        for character in question_three:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
    elif player_race.lower() not in valid_race:
            print('Sorry, the acceptable races are human, elf or dwarf. Please enter valid race.\n')
            question_two = 'What race are you?\n'
            question_twoadd = "(You can play as a human, elf or dwarf)\n"
            for character in question_two:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            for character in question_twoadd:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.01)
            player_race = input(">")
            valid_race = ['human', 'elf', 'dwarf']
            if player_race.lower() in valid_race:
                myplayer.race = player_race
                print("You are a " + player_race + ".\n")
                question_three = 'Hello ' + player_name + '!\n'
                for character in question_three:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)


    """After player inputs name and race, the intro for the game prints"""

    intro1 = "Welcome to the world of Phaladin!\n"
    intro2 = "You start this journey waking up in a large castle unaware of how you got there.\n"
    intro3 = "Of course, you look for an open door or window to jump out of in order to escape.\n"
    intro4 = "Unfortunately, there are no windows and the door is locked shut and won't budge no matter how hard you push.\n"
    intro5 = "Your first task in this fantasy world is to find a way out! Good luck.\n"

    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)



###Game Start###
    os.system('clear')
    print('****')
    print('Game Start')
    print('***')

def intro():

    """
    Parameters:
    arg1(int): input A
    :return: option_cautious goes into reading room

    arg2 (int): input B
    return: option_genki skips reading room, goes into hallway

    arg3 (int): input C
    return: option_angry stays in front entrance and prompts early conflict with monster

    arg4 (int): input check inventory
    returns: prints inventory and prompts player to pick next option
    """

    print("What do you want to do?")
    time.sleep(0.1)
    print('A. Look around. Where the hell am I?\n'
     'B. Run forward! I can escape this castle. No sweat! \n'
     'C. Try to bust down the door. The narrator knows not of my strength.\n')
    choice=input(">")
    if choice in answer_A:
        option_cautious()
    elif choice in answer_B:
        option_genki()
    elif choice in answer_C:
        option_angry()
    elif choice in answer_F:
        check_inventory()
        choice=input(">")
        if choice in answer_A:
            option_cautious()
        elif choice in answer_B:
            option_genki()
        elif choice in answer_C:
            option_angry()
    else:
        print("Please enter A, B, C, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            option_cautious()
        elif choice in answer_B:
            option_genki()
        elif choice in answer_C:
            option_angry()

def option_cautious():
    """
    Player is in the reading room; grocery list can be added to inventory in this room
    Parameters:
    arg1(int): input A
    :return: option_forward; player doesn't unveil grocery list; goes into hallway

    arg2 (int): input B
    return: option_reading; player unveils grocery list and is added to inventory; goes into hallway


    arg4 (int): input check inventory
    returns: prints inventory and prompts player to pick next option
    """
    print("Your eyes move from the impenetrable steel of the entrance to your bare surroundings.\n"
          "Listening carefully, you detect no presence as you move into the next room.\n"
          "This room seems to be a den of some kind. It is dimly lit with candles, shelves of books line the wall, and a large comfy chair lounges in the corner.\n")
    time.sleep(0.01)
    print("What do you want to do?\n")
    time.sleep(0.01)
    print("A. Keep moving forward. This is no time for dawdling!\n"
    "B. Take a closer look at these books. I wouldn't mind taking a quick break for some reading...\n")
    time.sleep(0.01)
    choice=input(">")
    if choice in answer_A:
        option_forward()
    elif choice in answer_B:
        option_reading()
    elif choice in answer_F:
        check_inventory()
        choice=input(">")
        if choice in answer_A:
            option_forward()
        elif choice in answer_B:
            option_reading()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            option_forward()
        elif choice in answer_B:
            option_reading()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                option_forward()
            elif choice in answer_B:
                option_reading()



def option_genki():
    """
      Player is in hallway:
      arg1(int): input A
      :return: prints text; run option_crossroads; player doesn't meet monster

      arg2 (int): input B
      return: prints text; run option_attack; player meets monster


      arg4 (int): input check inventory
      returns: prints inventory and prompts player to pick next option
      """
    print("You don't look back as you run from the front entrance into the next room. A blur of wooden floors, a chair, ...maybe books?\n"
          "You shrug and enter into a long dark hallway. The hallway is dimly lit with torches and paintings line the wall.\n")
    print("Would you care to look around?")
    print("A. Not really. Not much to look around for.\n"
          "B. Why not? All I have is time...well...and this sword.\n")
    choice=input(">")
    if choice in answer_A:
        print("You walk down the long hall and open the door to reveal an empty space with two doors.")
        cross_roads()
    elif choice in answer_B:
        print("You slowly walk down the dark hall\n"
              "You gaze at the portraits who look down at you judgingly as you walk by.\n"
              "You here a slithering sound behind you.\n")
        option_attack()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            cross_roads()
        elif choice in answer_B:
            option_attack()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            cross_roads()
        elif choice in answer_B:
            option_attack()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                cross_roads()
            elif choice in answer_B:
                option_attack()

def option_angry():
    """Player is in front entrance: prints text; meets monster and run option_attack"""
    print("You unsheath your sword and begin to slash at the door with all your might\n"
          "The door doesn't budge. You grow more and more frustrated\n")
    print("You turn on your heel skipping through the room full of books into a dark hallway\n")
    print("You hear a slithering.\n")
    option_attack()

def option_forward():
    """
          Player is in hallway; meets monster
          arg1(int): input A
          :return: prints text; run option_attack; player prepares to attack monster

          arg2 (int): input B
          return: prints text; run ask1; player meets monster and asks question

          arg4 (int): input check inventory
          returns: prints inventory and prompts player to pick next option
          """
    print("You march on forward. A person of your calibar would not dare be lazing around when work needed to be done.\n"
          "You exit out through the only door into a long dark hallway. The faces of potraits judgingly stare at you as walk past.\n"
          "You only hear the small crackling of the torches that hang on the wall that barely light your path.\n"
          'Does this path ever end? You mused in your head.\n'
          '"Who knows?", a voice answers.\n')
    time.sleep(0.01)
    print ("What do you want to do?\n")
    time.sleep(0.01)
    print("A. Get ready for attack.\n"
          "B. Ask the voice a question.\n")
    time.sleep(0.01)
    choice=input(">")
    if choice in answer_A:
        option_attack()
    elif choice in answer_B:
        ask1()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            option_attack()
        elif choice in answer_B:
            ask1()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            option_attack()
        elif choice in answer_B:
            ask1()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                option_attack()
            elif choice in answer_B:
                ask1()

def grocery_list():
    """Player is in reading room: prints text; grocery list is added to inventory"""
    print("You unfold the paper carefully. It reads:\n"
          "Warning to those who are entrapped in this castle. A monster lives in these walls. You must help it.\n"
          "The rest is scribbled out except for the following list:\n"
          "Crushed nightshade, a pigs snout, and 3 drops of human blood\n")

    inventory['Grocery List']='Not sure exactly what this is for. Crushed nightshade, a pigs snout, and 3 drops of human blood? '
    print("You slide this paper into your armor for safe keeping.\n"
          "A new item has been added to your inventory!\n")

def option_reading():
    """
             Player is in reading room and then moves into hallway to meet monster; prints text; runs grocery list function

             arg1(int): input A
             :return: prints text; run ask2(); ask monster question

             arg2 (int): input B
             return: prints text; run option_attack; player meets monster and attacks

             arg4 (int): input check inventory
             returns: prints inventory and prompts player to pick next option
             """
    print("Your hands skim the worn out spines of hard-cover books.\n"
          "Your fingers stop when you notice a slim piece of paper hiding between 'The Study of Mystical Beasts' and 'How to Tame Pythons'")
    grocery_list()
    print("You no longer feel like reading instead you lounge in the chair for a quick 15 minute rest and head off to the next room.\n"
          "You enter into the next room. A long hallway lies before you.\n"
        "Among the cackling of the torches, you hear the constant dripping of water.\n"
        "You carefully step through a large puddle.\n"
        "Watch where you are going. A voice states.\n"
        "You quickly turn around which splashes the unknown liquid in the narrow space."
        "It bounces and sways never really gaining an entire being but rather acting like sand by shaping and reshaping into different limbs.\n"
        "You just stare in horror as it finally gains composure and sways in the dark light. It makes no moves towards you.\n"
        
        "What do you do?\n")
    print("A. This may be the creature from the note! Does it need your help?\n"
          "B. Get ready to attack\n")
    choice=input(">")
    if choice in answer_A:
        ask2()
    elif choice in answer_B:
        option_attack()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            ask2()
        elif choice in answer_B:
            option_attack()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            ask2()
        elif choice in answer_B:
            option_attack()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                ask2()
            elif choice in answer_B:
                option_attack()

def option_reading2():

    """This option only appears if the player didn't get the grocery list, goes back to the reading room, and decides to read the book ; print text,
    grocery_list function (add to dictionary), where_next function"""
    print("Your hands skim the worn out spines of hard-cover books.\n"
          "Your fingers stop when you notice a slim piece of paper hiding between 'The Study of Mystical Beasts' and 'How to Tame Pythons'")
    grocery_list()
    where_next()

def ask1():
    """In hallway

             arg1(int): input A
             :return: prints text; avoids conflict with monster; go to cross_roads

             arg2 (int): input B
             return: prints text; run option_attack; player meets monster and attacks
    """
    print("Be ye friend or foe? You ask\n"
          "The monster gives off a sound similar to a snort says nothing and slinks away")
    print("What do you want to do?\n"
          "A. Head down the hall\n"
          "B. Attack the monster\n")
    choice=input(">")
    if choice in answer_A:
        cross_roads()
    elif choice in answer_B:
        attack()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            cross_roads()
        elif choice in answer_B:
            attack()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            cross_roads()
        elif choice in answer_B:
            attack()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                cross_roads()
            elif choice in answer_B:
                attack()


def ask2():
    """In hallway; Happens if player has grocery list and decides to talk to monster; no conflict, run cross_roads"""
    print("Do you need my help? You ask with as much confidence you could muster under the looming of this monster\n"
          "The monster almost seems stunned. It doesn't immediately answer. You watch as the monster sways under its own weight, deforming and forming.\n"
          "...Pray tell, how will you do such as thing? It finally asks.\n"
          "You are hesitant to tell it of the scribbled paper you found.\n"
          "Stumbling over your own words, you begin to tremble. Should you prepare to fight? Should you run away?\n"
          'The monster notices this.\n"'
          'Oh please. We will not eat you or kill you if you do not plan to do the same to us. Go as you wish to the rest of the castle.\n '
          'It is refreshing to see a new face. Less of those recently. If you need us, we will be here.\n')
    print('The monster slinked away and with a great splash returned to its liquid form')
    print('You quickly run to the other side of the hallway, fearing the monster will change its mind\n'
          "You open the door into an open space leading into two directions\n")
    cross_roads()


def option_attack():
    """Player is currently attacking monster; this will result in death of monster/player
     arg1(int): input A
             :return: prints text; attack conflict with monster;

             arg2 (int): input B
             return: prints text; run option_run
    """
    print("Your hand grasped your weapon. Ready to fight it at any moment.\n"
          "Oh ho! How interesting. You think you can take me? ,the voice chuckles.\n"
          "Where are you? Come out and I may spare your life, you command.\n"
          "The voice doesnot answer. The room goes silent with even the cackling of the torches becoming barely audible whispers. The thumping of your heart echoes in your ear.\n "
          "As you shuffle your feet to adjust your position, you hear a soft wet squishing.\n")
    time.sleep(0.05)
    print("You quickly turn around which splashes the unknown liquid in the narrow space. It seems to bubble up and rolls on top of one another forming a giant mass.\n"
          "It bounces and sways never really gaining an entire being but rather acting like sand by shaping and reshaping into different limbs.\n"
          "You just stare in horror as it finally gains composure and sways in the light. It makes no moves towards you.\n"
          "What do you do?\n")
    time.sleep(0.01)
    print("A. Attack.\n"
          "B. Run Away\n")
    time.sleep(0.01)
    choice = input(">")
    if choice in answer_A:
        attack()
    elif choice in answer_B:
        option_run()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            attack()
        elif choice in answer_B:
            option_run()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            attack()
        elif choice in answer_B:
            option_run()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                attack()
            elif choice in answer_B:
                option_run()

def cross_roads():
    """Player left hallway into an empty space between two rooms

      arg1(int): input A
             :return: option_parlor

             arg2 (int): input B
             return: prints text; option_dining room
    """
    print( "You can go left or right")
    print("Which do you choose?\n"
          "A. Right\n"
          "B.Left\n")
    choice=input(">")
    if choice in answer_A:
        option_parlor()
    elif choice in answer_B:
        dining_room()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            option_parlor()
        elif choice in answer_B:
            dining_room()
    else:
        print("Please enter A, B,  or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            option_parlor()
        elif choice in answer_B:
            dining_room()
        elif choice in answer_F:
            check_inventory()
        choice = input(">")
        if choice in answer_A:
            option_parlor()
        elif choice in answer_B:
            dining_room()

def option_parlor():
    """Player turned right at cross roads currently in parlor
        arg1(int): input A
        return: prints text; do not drink; run dining_room

        arg2 (int): input B
        return: prints text; drink; prompts puzzle
       """
    print("You open the door to a beautiful sitting area, complete with a small table adorned with a beautiful crystal glass filled with a dark brown liquid. A small note is propped beside it: Drink me.\n")
    print("As you walk closer, you notice that there is a small box. You quickly try to open it but realize it needs a key.\n")
    print("You move over to the glass and pick it up.\n"
          "Do you take a drink?\n"
          "A. What are you crazy?! No!\n"
          "B. Sure. What have I got to lose?")
    choice=input(">")
    if choice in answer_A:
        print("You put the glass down, scan over the room but realize nothing is left to investigate.\n")
        print("You exit and go into the other room\n")
        dining_room()
    elif choice in answer_B:
        drink_up()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            dining_room()
        elif choice in answer_B:
            drink_up()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            dining_room()
        elif choice in answer_B:
            drink_up()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                dining_room()
            elif choice in answer_B:
                drink_up()


def drink_up():
    """Prompts puzzle; answer is LOOK BEHIND RED PILLOW; needs to correctly answer puzzle to continue game; when answered correctly
    nail and bowl are added to inventory """
    print("You give the glass a quick sniff. A harsh aroma fills your nostrils.\n" 
              "You raise the glass in a unrequitted cheers and chug the liquid. You could use it after the day you have had.\n"
              "The drink is strong. You give one hefty cough and lift the glass to inspect it. Nothing.\n"
              "You pick up the note to inspect it more clearly. The backside has scrambled words:")
    print("KLOO\n"
              "HDBENI\n"
               "DRE\n"
               "WLLIPO\n")
    print("What does it say?")
    choice=input(">")
    if choice in answer_puzzle:
        print("You do as the note instructs. You find the red pillow sitting neatly on a small chair. Sure enough, there is a small key.\n"
                "You open the box. There is small nail and a bowl.\n")
        inventory['Nail'] = 'This nail is sharp. Got to be careful not to prick myself.'
        inventory['Bowl']='A large bowl. Is it meant to hold something?'
        print("You hold unto the nail and bowl for safe keeping.\n"
              "Two new items have been added to your inventory!\n")
        print("You scan over the room but realize nothing is left to investigate.\n")
        print("You exit and go into the other room\n")
        dining_room()
    while choice not in answer_puzzle:
        print ("That's not quite right. Unscramble the words line by line. Try again.")
        print("KLOO\n"
              "HDBENI\n"
               "DRE\n"
               "WLLIPO\n")
        print("What does it say?")
        choice = input(">")
        if choice in answer_puzzle:
            print(
                "You do as the note instructs. You find the red pillow sitting neatly on a small chair. Sure enough, there is a small key.\n"
                "You open the box. There is small nail and a bowl.\n")
            inventory['Nail'] = 'This nail is sharp. Got to be careful not to prick myself.'
            inventory['Bowl'] = 'A large bowl. Is it meant to hold something?'
            print("You hold unto the nail and bowl for safe keeping.\n"
                  "Two new items have been added to your inventory!\n")
            print("You scan over the room but realize nothing is left to investigate.\n")
            print("You exit and go into the other room\n")
            dining_room()

def dining_room():
    """Player is in dining room
            arg1(int): grocery list is in inventory and monster is alive
            return: snout is added to inventory; prompts choice to ask monster for last ingredient or continue looking around castle
                arg1.5 (int): input A (player must have grocery list, snout, and nail/bowl)
                return: ask3
                arg 1.6 (int): input B (player doesn't have all items)
                return: where next

            arg2 (int): grocery list is in inventory and monster is dead
            return: bad end

            arg3: grocery list is NOT in inventory and monster is alive
            return: print "not sure...."

            arg4: snout is in inventory
            return: print not much to do here
           """
    print("You open the door to a large banquet hall\n"
          "Your stomach rumbles in response to a slight aroma in the air\n")
    print("Your nose leads you to the only decorated table where a large cooked pig lies- snout and all\n"
          "Steam rises from the meat as if it was just removed from the fire pit\n")
    if 'Grocery List' in inventory and monsterhp>0:
        print("You pull out your sword and cut the snout off the pig\n")
        inventory['Snout']='Ew...it is a pig snout.'
        print("As you do so, a small piece of paper falls out of the nasal cavity unto the bed of lettuce underneath it\n"
              "You pick up the note\n"
              "It reads: Ask the monster for one of the ingredients\n"
              "What do you want to do\n"
              "A. Go ask the monster for the ingredient (if all completed)\n"
              "B. Go check another room\n")
        choice=input(">")
        if choice in answer_A and 'Snout' in inventory and 'Nail' in inventory:
            ask3()
        elif choice in answer_B:
           where_next()
        elif choice in answer_F:
            check_inventory()
            dining_room()
    if monsterhp<0 and 'Grocery List' in inventory:
        bad_end()
    elif 'Snout' in inventory:
        print("Not really much to do here...\n")
        where_next()
    elif 'Grocery List' not in inventory:
        print("You are unsure of what to do here...")
        where_next()

    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A and 'Snout' in inventory and 'Nail' in inventory:
            ask3()
        elif choice in answer_B:
            where_next()
        elif choice in answer_F:
            check_inventory()
            dining_room()
    if monsterhp < 0 and 'Grocery List' in inventory:
        bad_end()
    elif 'Snout' in inventory:
        print("Not really much to do here...\n")
        where_next()
    elif 'Grocery List' not in inventory:
        print("You are unsure of what to do here...")
        where_next()



def ask3():
    """Player is in hallway to ask monster for nightshade/tomato
               arg1(int): A
               return: print text, monster gives you nightshade, you win!!

                arg2 (int): B
               return: option_attack
"""
    print("Your footsteps echo in the hallway.\n"
          "You call out for the monster\n"
          "It appears before you\n"
          "What do you want?\n")
    print("What do you do?\n")
    print("A. Ask the monster for night shade\n"
          "B Attack the monster\n")
    choice=input(">")
    if choice in answer_A:
        print("The monster stands still for a second\n"
              "It then begins to convulse and shake\n"
              "A round object pops out of an orfice into your hands\n"
              "You take a closer look\n"
              "It's a tomato\n")
        good_end()
    if choice in answer_B:
        option_attack()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            print("The monster stands still for a second\n"
                  "It then begins to convulse and shake\n"
                  "A round object pops out of an orfice into your hands\n"
                  "You take a closer look\n"
                  "It's a tomato\n")
            good_end()
        if choice in answer_B:
            option_attack()


####These options are specifically for the where_next function (if player has not explored each room and collected all items)

def where_next():

    """If player did not collect all items, they will be prompted to visit the rooms again and explore to find the items
        arg1(int): A
               return: front entrance

        arg2 (int): B
               return: den (with books)

        arg1(int): C
               return: hallway2

        arg2 (int): D
               return: parlor

        arg1(int): E
               return: dining room

       """
    print("Where would you like to go?\n"
          "A. The Front Entrance\n"
          "B. The den (with books)\n"
          "C. The dark hallway\n"
          "D. The fancy sitting room (right door at cross roads)\n"
          "E. Dining Room\n")
    choice=input(">")
    if choice in answer_A:
        front_entrance()
    elif choice in answer_B:
        den()
    elif choice in answer_C:
        hallway2()
    elif choice in answer_D:
        parlor()
    elif choice in answer_E:
        dining_room()
    elif choice in answer_F:
        check_inventory()
        choice = input(">")
        if choice in answer_A:
            front_entrance()
        elif choice in answer_B:
            den()
        elif choice in answer_C:
            hallway2()
        elif choice in answer_D:
            parlor()
        elif choice in answer_E:
            dining_room()
    else:
        print("Please enter A, B, or Check Inventory")
        choice = input(">")
        if choice in answer_A:
            front_entrance()
        elif choice in answer_B:
            den()
        elif choice in answer_C:
            hallway2()
        elif choice in answer_D:
            parlor()
        elif choice in answer_E:
            dining_room()

def hallway2():
    """Hallway (meeting initial with monster)
            arg1(int): A and monster alive
                   return: attack monster; option_attack

            arg2 (int): B and monster is alive
                   return: ask monster a question; where_next

            arg1(int): if monster is dead
                   return: print nothing important is here; where_next"""
    if monsterhp>0:
        print("You exit out through the only door into a long dark hallway. The faces of potraits judgingly stare at you as walk past.\n"
          "You only hear the small crackling of the torches that hang on the wall that barely light your path.\n"
          'Does this path ever end? You mused in your head.\n'
          '"Who knows?", a voice answers.\n')
        print("What do you do?\n")
        print("A. Get ready to attack\n"
          "B. Call out to the monster\n")
        choice=input(">")
        if choice in answer_A:
            option_attack()
        elif choice in answer_B:
            print("Be ye friend or foe? You ask.\n"
            "The monster gives off a sound similar to a snort says nothing and slinks away\n")
            where_next()
    elif monsterhp<=0:
        print("The hallway is quiet\n")
        print("Nothing important is here\n")
        where_next()



def front_entrance():
    """Player goes to front entrance, nothing is there,prompts where_next function"""
    print("You head back to where it first started.\n"
          "You scan the area but it seems bare.\n"
          "You knock on the large metal door but it does not budge\n")
    where_next()


def den():
    """Den (reading room)
                arg1(int): A read books
                       return: option_reading2; grocery list added to inventory

                arg2 (int): B leave
                       return: where_next function

                arg1(int): if grocery list is already in inventory
                       return: there is nothing left here; where next function """
    if 'Grocery List' in inventory:
        print("There is nothing left to look for in this room\n")
        where_next()
    else:
        print("What would you like to do?\n"
              "A. Let's take a look at these books\n"
              "B. Eh...Let's look somewhere else\n")
        choice=input(">")
        if choice in answer_A:
            option_reading2()
        elif choice in answer_B:
            where_next()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                option_reading2()
            elif choice in answer_B:
                where_next()
        else:
            print("Please enter A, B, or Check Inventory")
            choice = input(">")
            if choice in answer_A:
                option_reading2()
            elif choice in answer_B:
                where_next()
            elif choice in answer_F:
                check_inventory()
                choice = input(">")
                if choice in answer_A:
                    option_reading2()
                elif choice in answer_B:
                    where_next()

def parlor():
    """Parlor/Sitting room (meeting initial with monster)
               arg1(int): A drink liquid
                      return: drink liquid and prompts puzzle to get nail and bowl

               arg2 (int): B do not drink liquid
                      return: do not drink liquid; where_next
                      """
    if "Nail" in inventory:
        print("There is nothing left to look for in this room\n")
        where_next()
    else:
        print("You open the door to a beautiful sitting area, complete with a small table adorned with a beautiful crystal glass filled with a dark brown liquid. A small note is propped beside it: Drink me.\n")
        print("As you walk closer, you notice that there is a small box. You quickly try to open it but realize it needs a key.\n")
        print("What would you like to do?\n")
        print("A. I'm thirsty! Let's drink the brown liquid\n"
              "B. I don't like the look of this room...Let's go somehwere else.\n")
        choice=input(">")
        if choice in answer_A:
            drink_up()
        elif choice in answer_B:
            where_next()
        elif choice in answer_F:
            check_inventory()
            choice = input(">")
            if choice in answer_A:
                drink_up()
            elif choice in answer_B:
                where_next()
        else:
            print("Please enter A, B, or Check Inventory")
            choice = input(">")
            if choice in answer_A:
                drink_up()
            elif choice in answer_B:
                where_next()
            elif choice in answer_F:
                check_inventory()
                choice = input(">")
                if choice in answer_A:
                    drink_up()
                elif choice in answer_B:
                    where_next()













###GAME START##
## Loop needed to continue game until puzzle is solved, everything is inspected, etc. ##
title_screen()
intro()

    



