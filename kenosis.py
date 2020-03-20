#imports the time library for time.sleep
import time
class setup:
    #This is the start-up intro. It displays the intro text and checks whether or not the user would like to play the intro, then inits the game/tutorial.
    def startup():
        startupe = """
         _        _______  _        _______  _______ _________ _______ 
        | \    /\(  ____ \( (    /|(  ___  )(  ____ \\__   __/(  ____ \.
        |  \  / /| (    \/|  \  ( || (   ) || (    \/   ) (   | (    \/
        |  (_/ / | (__    |   \ | || |   | || (_____    | |   | (_____ 
        |   _ (  |  __)   | (\ \) || |   | |(_____  )   | |   (_____  )
        |  ( \ \ | (      | | \   || |   | |      ) |   | |         ) |
        |  /  \ \| (____/\| )  \  || (___) |/\____) |___) (___/\____) |
        |_/    \/(_______/|/    )_)(_______)\_______)\_______/\_______)

        (C) Nathanial Landers & Leyton Frecklington 2020
        """
        print(startupe)
        print("Would you like to play the tutorial (Recommended)? (Y/N)")
        playTutorial = input(">> ")
        if playTutorial == 'y' or playTutorial == 'Y' or playTutorial == 'yea' or playTutorial == 'yes':
            tutorial.tutorialintro()
        else:
            game.l1game()
#Class that contains all of the tutorial including logic and intro. Also includes the specific exit command for this section, as the N result will change.
class tutorial:
    #This is an exit command. It closes the game, or continues the game depending on a Y/N answer.
    def exitt():
            print("Are you sure? (Y/N)")
            exit = input(">>> ")
            if exit == 'Y' or exit == 'y' or exit == 'yes' or exit == 'yea':
                exit()
            else:
                tutorial.tutorialroom()
    #Variables required for inventory. This is improved later in the game class, but for only one item in this level, it is sufficient.
    coins = 0
    pickupcoinsused = 0
    
    # All of the commands used in the tutorial sequence. this is improved and simplified into one definition later in the game class.
    #self explantory, ends the tutorial and loads the actual game.
    def endtutorial():
        print("Starting Kenosis...")
        time.sleep(2)
        game.l1game()
    #reprints the intro. Does not reset the game.
    def where():
        tutorial.tutorialintro()
    #use coins, checks if in inv or if used
    def usecoins():
        if tutorial.coins == 1:
            print("You throw the coins across the room.")
            tutorial.coins = 0
            tutorial.pickupcoinsused = 0
            tutorial.tutorialroom()
        else:
            print("You don't have coins.")
        time.sleep(2)
        tutorial.tutorialroom()
    # look's are self explantory, prints info, waits, calls for the input & processing again.
    def looksign():
        print("You look at the sign. The sign reads: 'Tutorial'.")
        time.sleep(2)
        tutorial.tutorialroom()
    def lookall():
        print("You look at your surroundings. You see: sign, chair, table, window, coins.")
        time.sleep(2)
        tutorial.tutorialroom()
    def lookchair():
        print("You inspect the chair. It's just a wooden chair. It's starting to decay from rot.")
        time.sleep(2)
        tutorial.tutorialroom()
    def looktable():
        print("You inspect the table. It's just a wooden table. It's starting to decay from rot.")
        time.sleep(1)
        tutorial.tutorialroom()
    def lookwindow():
        print("You look out the window. It's pitch black, you can't see anything.")
        tutorial.tutorialroom()
    def pickupwindow():
        print("You can't pick-up the window.")
        time.sleep(2)
        tutorial.tutorialroom()
    def pickupchair():
        print("You try to pick-up the chair. You are weak, and it is too heavy.")
        time.sleep(2)
        tutorial.tutorialroom()
    def pickuptable():
        print("You try to pick-up the table. You are weak, and it is too heavy.")
        time.sleep(2)
        tutorial.tutorialroom()
    def pickupchair():
        print("You try to pick-up the chair. You are weak, and it is too heavy.")
        time.sleep(2)
        tutorial.tutorialroom()
    def usechair():
        print("You try to sit down on the chair. You are too heavy for the rotted chair, and it creaks under your weight. You feel it flexing, and decide to get back up.")
        time.sleep(2)
        tutorial.tutorialroom()
    def usetable():
        print("You try to sit on the table. It creaks, and warps the rotting wood. You decide to get back up.")
        time.sleep(2)
    def pickupsign():
        print("You try to pick-up the sign, but your weak ginger arms cannot muster the strength to pick it up. You give up.")
        time.sleep(2)
        tutorial.tutorialroom()
        tutorial.tutorialroom()
        #easter egg lol
    def usewindow():
        print("You manage to open the window, and climb outside. You hear whispers in your head. All you can hear is the word Craig.")
        time.sleep(1)
        print("Craig.")
        print("Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig.")
        print("Craig.")
        print("Craig.")
        print("Craig.")
        print(game.crag)
        print("Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. Craig. ")
        print("Craig. Craig. Craig. Craig. Craig. .giarCCraig. Craig. Craig. Craig. Craig. .giarC")
        print("Craig.")
        print("Craig.")
        print("Craig.")
        print("Craig.")
        print("Craig.")
        print("You die.")
        time.sleep(2)
        tutorial.tutorialintro()
    #improvements added later
    def lookcoins():
        print("You look at the coins. They are Australian 20 cent coins.")
        time.sleep(2)
        tutorial.tutorialroom()
    def usesign():
        print("You try and use the sign. You see a note under it: use the window.")
        tutorial.tutorialroom()
    # Pick-up commands.
    def pickupcoins():
        if tutorial.pickupcoinsused == 0:
            print("You pick-up the coins, and place them in your pocket.")
            tutorial.coins = 1
            tutorial.pickupcoinsused = 1
            tutorial.tutorialroom()
        else:
            print("You already have the coins.")
            tutorial.tutorialroom()



    # Inventory
    def inventory():
        
        if tutorial.coins == 0:
            print("You have nothing in your inventory.")
        if tutorial.coins == 1:
            print("You check your pockets, and you find: Coins.")
        tutorial.tutorialroom()



    # Tutorial Intro. This is only played once, but calls for logic afterwards.
    def tutorialintro():
            print('Starting Tutorial...')
            print("")
            time.sleep(3)
            print("You awake in a dark room. Ahead is a wall, with a bright neon sign hanging on it. There is also a table, chair, window and some coins on the floor.")
            print("")
            time.sleep(3)
            print("Welcome to the tutorial. You can test the various commands that you will use in Kenosis to navigate, interact and inspect.")
            print("")
            time.sleep(3)
            print("These commands are: look, pick-up, where, inventory.")
            print("")
            time.sleep(3)
            print("The 'look' command let's you look at an object, or all objects. First try 'look all' to list all objects in a room, then 'look (obj)' to inspect it.")
            print("")
            time.sleep(3)
            print("The 'pick-up' command allows you to pick up an object. This will only happen on objects you can pick up though. Try 'pick-up (obj)'.")
            print("")
            time.sleep(3)
            print("The 'where' command repeats the scene opening, such as the 'Ahead is a wall, with a ...' at the start of this tutorial. Try 'where'.")
            print("")
            time.sleep(3)
            print("The 'inventory' command lists all items you have picked up. Try 'inventory'.")
            print("")
            time.sleep(3)
            print("The 'use' command allows you to use an object you have in your inventory. Try 'use (obj).")
            print("")
            time.sleep(3)
            print("Note: All commands are in lower-case.")
            print("")
            time.sleep(3)
            print("Try any of these commands in this tutorial sequence. When you are finished, type 'end tutorial'.")
            print("")
            tutorial.tutorialroom()       
# NOTE  : : : : : : : : : 
# we improved on the calling for different commands later. Since this sequence isn't very complex, we decided to keep this logic the same. For a better example, please see the game() class.
# :)
# NOTE  : : : : : : : : :
    
    def tutorialroom():
        #var
        choice = input(">> ")
        #game routine
        if 'exit' in choice:
            tutorial.exitt()
        if 'look sign' in choice:
            tutorial.looksign()
        if 'use sign' in choice:
            tutorial.usesign()
        if 'look coins' in choice:
            tutorial.lookcoins()
        if 'look chair' in choice:
            tutorial.lookchair()
        if 'look all' in choice:
            tutorial.lookall()
        if 'look window' in choice:
            tutorial.lookwindow()
        if 'look table' in choice:
            tutorial.looktable()
        if 'pick-up coins' in choice:
            tutorial.pickupcoins()
        if 'use coins' in choice:
            tutorial.usecoins()
        if 'inventory' in choice:
            tutorial.inventory()
        if 'where' in choice:
            tutorial.where()
        if 'end tutorial' in choice:
            tutorial.endtutorial()
        if 'use table' in choice:
            tutorial.usetable()
        if 'use chair' in choice:
            tutorial.usechair()
        if 'use window' in choice:
            tutorial.usewindow()
        if 'pick-up table' in choice:
            tutorial.pickuptable()
        if 'pick-up chair' in choice:
            tutorial.pickupchair()
        if 'pick-up window' in choice:
            tutorial.pickupwindow()
        if 'pick-up sign' in choice:
            tutorial.pickupsign()
        if 'pickup sign' in choice:
            tutorial.pickupsign()
        if 'pickup table' in choice:
            tutorial.pickuptable()
        if 'pickup chair' in choice:
            tutorial.pickupchair()
        if 'pickup window' in choice:
            tutorial.pickupwindow()
        else:
            print("I didn't understand what you meant. Try again.")
            tutorial.tutorialroom()

class game:
    def exit():
        print("Are you sure? (Y/N)")
        exit = input(">>> ")
        if exit == 'Y':
            exit()
        elif exit == 'y':
            exit()
        else:
            game.logic()
    #Progression Variables + Unused variables that might be used later
    inventorys = []
    spoonlock = 1
    spoon = 0
    stick = 0
    necklace = 0
    matches = 3
    cansee = 0
# inventory
    def inventory():
        print("You check your pockets, and find:")
        print(*game.inventorys, sep = ", ")
        game.logic()
        
       
  
    
    
    
    
    
    
    #Art
    crag = """
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,********************
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**************
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***********
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**,,***
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,....,,/(*&&%&*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,.,../#%#(##%%&%&&&%&&&%(*,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,###%#%%%%&&&&&&&&&&&&&&&%,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,*((#&&&%/*//(#(///((#&@&&%%%*,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,...,..,,,,,,,,,.,,*//#%&#*,,******//////((&@@@&#/,,,,,,,,,,,,,,,,,,,,,,,,
.......,,,,,.,,,,.......,,*((#(***********////////%%%&%(,,,,,,,,,,,,,,,,,,,,,,,,
..........................,#%(************/////////%%%%(,,,,,,,,,,,,,,,,,,,,,,,,
...................,....,,,,,/*****/*****///*//***//#%%/,,,,,,,,,,,,,,,,,,,,,,,,
..........................,,*/*//((((////((((////////#(#,,,,,,,,,,,,,,,,,,,,,,,,
...........................,/(**(#%OO(**/((((((OO////((#,,,,,,,,,,,,,,,,,,,,,,,,
............................./****//****//////////**/#*(,,,,,,,,,,,,,,,,,,,,,,,,
.............................*****//(**/////#((///////(,,,,,,,,,,,,,,,,,,,,,,,,,
...............................*/((((/(###(((##((////,,,,,,,,,,,,,,,,,,,,,,,,...
...............................**//(/((#(##%&#/(////*,.,,,,,,,,,,,,,,,,,,,,,,,,.
................................***///////((////////..,,,,,,,,,,,,,,,,,,,,,,,,,.
................................./****////////*////@@,,,,,,,,,,,,,,,,,,,,,,,,,,.
...............................,&&*/***////////////@@&,,,,,,,,,,,,,,,,,,,,,,,,..
.........................,,,(%%%&&%**/#%#####/////#@&&&%&#/,,,,.......,,,,,,,,,,
.....................,((%(%%###&&&&(/*//((///////#&@&&&%%%%&%%%%#,........,,,,,,
..............,#######%%#%&####&%%%#%&#(((/////#%&@@&&&&&%%%&%%%%%%%##%#/,,.,,,,
..............#####%%%#%#&%####%&&%%@@&&#((//((%&@@&&&&&%&%%%%%&%%%%%%%%##,,....
............%%###%%%%%%%%%%#%##%%&&&&@@&&&((((#@@@&&&&&@&&%%%%%&&%%%%%%%%##,,...
...........%&&#%%%%%%%%%%%%%%%%%%&&&%&@@&&&##@@@&%&&&&%&&&%%%%%&&&%%%%%%%%@%,,..
.........#%&&&#%%#%%%%%%%%%%%%%%%%&&&%%&@&&&@@@&&&%&&%%&&&%%%%%&&&%%%%%%%%@&%,,,
........%%&&&&#%%##%%%%%%%%%%%%%%%&&&&%&&&&&@@&&&%%&&%%&&&%%%%%%%&%%%%%%%%@@&%%,
.......%&&@&&&#%%%%%%%%%%%%%%%%%%%&&&&%%@&&&&@&&&&&&&&&&&&%%%%%%&%%%%%%%%%@@&&&&
......%&&&@@&&#%%#%%%%%%%%%%%%%%%%%&&&&%%&&&&@&&%%&%&%%%%%%%%%%%&%%%%%%%%%@@&&&&
"""
    necklace = """
   
WW:WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@:WWW
W@:WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#+WWW
W*=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:@WWW
WW:#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+WWWW
WWW:@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW-@WWWW
WWWW+=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:#WWWWW
WWWWW@:@WWWWWWWWWWWWWWWWWWWWWWWWWWW*+WWWWWWW
WWWWWWWW++@WWWWWWWWWWWWWWWWWWWWWW=+WWWWWWWWW
WWWWWWWWWWW*:=WWWWWWWWWWWWWWWWW=:WWWWWWWWWWW
WWWWWWWWWWWWWWW@=++*=#@@@@=+:=WWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW*=@:@WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW*.*WWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWW-...................-WWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW...#WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW...@WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW-..WWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW-..WWWWWWWWWWWWWWWWWWWw
WWWWWWWWWWWWWWWWWWWWW:..WWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW:..WWWWWWWWWWWWWWWWWWWW
    """
    stick = """
WWWWWWWWWWW==WWWWWWWWWWWWWW
WWWWWWWWWW@..=WWWWWWWWWWWWW
WWWWWWWWWWW+.-WWWWWWWWWWWWW
WWWWWWWWWWW@..=WWWWWWWWWWWW
WWWWWWWWWW@W+.+WWWWWWWWWWWW
WWWWWWWWW#.:=.-WWWWWWWWWWWW
WWWWWWWWWW=....*WWWWWWWWWWW
WWWWWWWWWWW:....WWWWWWWWWWW
WWWWWWWWWWWWW*..@WWWWWWWWWW
WWWWWWWWWWWWW=..WWWWWWWWWWW
WWWWWWWWWWWWW+..WWWWWWWWWWW
WWWWWWWWWWWWW..+WWWWWWWWWWW
WWWWWWWWWWWW=.-WWWWWWWWWWWW
WWWWWWWWWWWW:.#WWWWWWWWWWWW
WWWWWWWWWWW=.:WWWWWWWWWWWWW
WWWWWWWWWWW-.=WWWWWWWWWWWWW
WWWWWWWWWW@..@WWWWWWWWWWWWW
WWWWWWWWWW=..WWWWWWWWWWWWWW
    """
    spoon = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=+:-----+=WWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@-............-@WWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW-...............*WW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW-...............:WW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#-..............=WW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=-...............+WWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*.........-+:....-*@WWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*.........-=WWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWW@+.........-=WWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWW#:.........+@WWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW#-........-*WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW#-.........:@WWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWW=-.........:#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWW@+..........:#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWW=........+#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWW#===@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    """
    lock = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWW@#=**#WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW+..+=*..-WWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWW=..#WWWW*..=WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWW..@WWWWWW-.:WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW*.*WWWWWWW*.-WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW=.-WWWWWWWW#..WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW*.+WWWWWWWW@..@WWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW@W*.=WWWWWWWW@..@WWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWW:................#WWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW#.................@WWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW+................:WWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWW-................+WWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW#.................#WWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW+................-WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW*+:-.............*WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    """
    matchbox = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  @@%    ,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(   (@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@(  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  / (@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@  @@@@@@@@@
@@@@@@@@@@@@@@@@@@%  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@  @@@@@@@@@
@@@@@@@@@@@@@@@%  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  @@@@@@@%  @@@@@@@@@
@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@@
@@@@@@@@@@@  @@@  @@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ,@@@@@@@   @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@        @@    @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@  (@  @@@     @   (@@@@@@@@@@@@@   @@@@@@@@  @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@  @@  @@    @@@@@@@        @@@@@@  @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@  &@@@@,  @@@@@&   ,@@@@@@@@&       @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@   @@@@   @@@@@@@@@@@, *     @@@@@@@@% .@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@   @@@@@@@@@@@@  @@@@  @@    @@@@@  ,   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@(   %@@@@@  @@@(  @@@&  @@@(   @, @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%   %@@@@&  @@@@  @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@     @@@@  @@@@(  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
    axe = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@                                                             @@@@@@@@@@@@@@@@@
@@                                                               @@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(        @@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               #*@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/*                      @@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/ /                         %@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@ @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @/                                      /@ @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@ @@@@@@@ @@@@@@  #@@@ @@@@ @@@@@*@@@ @@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@   .@@@@@@@. @@@@@@  @@@/@@@@@@@@@@*@@ @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@ ,@@@@@@ @@@@@@@(*@@@@ @@@@@@/@@@@@@ @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                             @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
"""
    keys = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%% %@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@%@ @@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@     @ @@@@ @@@@   @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@    @@@@((&  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@# @@@@@@@@@@@@@@@ @@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@( %@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@% (@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@% @@@@@@@@@@@@@@@@@
@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@% @@@@@@@@@@@@@@
@@@@@@( @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@, @@@@@@@@@@@
@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@   @ @@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   #@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@   &@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    rope = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,            (%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    @@@@@@@@@##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                     ,@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                       @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&/.       .*(&&&&&&@@@@@@@@@     (@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,                                 &@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@    .@@@@@@@@@((((((             @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%    .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@                                    ...*&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@(                                      @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#    @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*,,(###########################(,            @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*                                          *&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@(      (((((((((((((((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@.    .((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@(                                                      (@@@@@@@@@@@@
@@@@@@@@@@@@     @@@@(((/                                          @@@@@@@@@@@@@
@@@@@@@@@@@@.                ((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@((                                                        @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((((((((((((((((((((((((((,    %@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&     %@@@@@
@@@@@@@@@(                        .((((((#@@@@@@@@@@@@@@@@@              @@@@@@@
@@@@@@@@@@@(((((((((((((                                           *(@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/               .(%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    lockpick = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@&           /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@,               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@                    &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@(                      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@                       ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@                       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@                       *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%                       &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&                       (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&                        ,@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 ,@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      %@@@@/       @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@/      @@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          &@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          .@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    @@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    knife = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@.            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@*                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@&                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@                    %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    %@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                   #@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                @@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @          @@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@          @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,     &@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    bandages = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                             #  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                             @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@ &@ @ @@@ @@#@,@ @.          @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@ &@ @ @ @.@/@@,@ @.          @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@ %@@/.@ @@@*@@,@@(           @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                             @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@  @@%/@ @%@@*@@              @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@ &@@@/@ @%@@ @               @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@ @@.@/@ @@@.@@@              @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                             *   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    #Defines use commands
    # use stick all uses
    def usestickall():
        if "use stick bars" in choiceg:
            if "stick" in game.inventorys:
                print("You try to pry at the bars with the stick, but the stick is too thin and breaks before any bars are bent.")
                time.sleep(2)
                game.logic()
            else:
                print("You do not have a stick.")
                time.sleep(2)
                game.logic()
        elif "use stick lock" in choiceg:
            if "stick" in game.inventorys:
                print("You try to pick the lock with the stick, but the stick is too thick and can't fit in the lock mechanism.")
                time.sleep(2)
                game.logic()
            else:
                print("You do not have a stick.")
                time.sleep(2)
                game.logic()
        elif "use stick matchbox" in choiceg:
           if "stick" in game.inventorys: 
            if "matchbox" in game.inventorys:
                print("You try to light the stick on fire, and it works. You see some of the room around you.")
                game.cansee = game.cansee + 1
                time.sleep(2)
                game.logic()
            else: 
                print("You do not have a matchbox to use.")
                time.sleep(2)
                game.logic()
           else:
               print("You do not have a stick.")
               time.sleep(2)
               game.logic()

# use spoon logics
    def usespoonall():
        if "use spoon on lock" in choiceg:
            game.canuselock()
        if "use spoon lock" in choiceg:
            game.canuselock()
        if "use spoon in lock" in choiceg:
            game.canuselock()
        if "use spoon at lock" in choiceg:
            game.canuselock()
        if "use spoon bars" in choiceg:
            if 'spoon' in game.inventorys:
                print("You try to pry at the bars with the spoon, but it is too small to do anything with. You give up.")
                time.sleep(2)
                game.logic()
            else:
                print("You do not have a spoon")
                time.sleep(2)
                game.logic()

        if "use spoon matchbox" in choiceg:
            if game.matches >= 1:
                print("You heat up the spoon. Now you have a hot spoon. It does nothing.")
                matches = game.matches - 1
                time.sleep(2)
                game.logic()
            else:
                print("You are out of matches.")
                time.sleep(2)
                game.logic()
    def canuselock():
        if game.spoonlock == 1:
            game.usespoonlogic()
        else:
            print("You have already picked the lock.")
            time.sleep(2)
            game.logic()
   
           
            
            
    def usespoonlogic():
        if "spoon" in game.inventorys:
            if game.spoonlock == 1:
                print("You use the spoon on the lock. With a bit of time, you manage to pick the lock.")
                print("")
                time.sleep(2)
                game.spoonlock == 0
                game.logic()
            else:
                print("You have already unlocked the gate.")
                time.sleep(2)
                game.logic()
        else:
            print("You do not have a spoon.")
            time.sleep(2)
            game.logic()

    
 



    #Defines look commands
    def lookall():
         if 'where' in choiceg:
             game.l1game()
         if 'look crag' in choiceg:
            print(game.crag)
            game.logic()
         if 'look all' in choiceg:
             if game.cansee == 0:
                print("You feel around on the ground. You feel a few objects on the ground but it's too dark to know what they are, they feel like a stick, a matchbox and a necklace.")
                time.sleep(1)
                game.logic()
             elif game.cansee == 1:
                 print("You see some of the room around you. It's dark, but you can see the faint outline of a few objects on the ground.")
                 print('')
                 time.sleep(1)
                 print("You run your hand across the ground and find a stick, a spoon, a necklace and a matchbox.")
                 game.logic()
             else:
                game.logic()

         if "look necklace" in choiceg:
            print(game.necklace)
            print("You look at the necklace. It is made of a thin, linked chain and a wooden crucifix hanging off it, one side of it appears to be sharper than the others.")
            game.logic()
         if "look stick" in choiceg:
            print(game.stick)
            print("You look at the stick. It's a stick.")
            game.logic()
         if "look matchbox" in choiceg:
            print(game.matchbox)
            print("You look at the matchbox, it contains 6 matches and the striking surface is worn down to almost nothing")
            game.logic()
         if "look spoon" in choiceg:
             print(game.spoon)
             print("You look at the spoon. It could maybe be used to pick a lock.")
             game.logic()
    #Defines pick-up commands
    def pickupall():
        if "pick-up stick" in choiceg:
            if "stick" not in game.inventorys:
                print(game.stick)
                print("You pick up the stick, and put it in your pocket.")
                game.inventorys.append("stick")
                time.sleep(2)
                game.logic()
            else:
                print("You already have a stick.")
                time.sleep(2)
                game.logic()

        if "pick-up spoon" in choiceg:
            if "spoon" not in game.inventorys:
                print(game.spoon)
                print("You pick up the spoon, and put it in your pocket.")
                game.inventorys.append("spoon")
                game.logic()
            else:
                print("You already have a spoon.")
                time.sleep(2)
                game.logic()

        if "pick-up matchbox" in choiceg:
            if "matchbox" not in game.inventorys:
                print(game.matchbox)
                print("You pick up the matchbox, and have a look inside. The matchbox only has 3 matches, and the striking surface seems worn.")
                game.inventorys.append("matchbox")
                game.logic()
            else:
                print("You already have a matchbox.")
                time.sleep(2)
                game.logic()
        if "pick-up necklace" in choiceg:
            if "necklace" not in game.inventorys:
                print(game.necklace)
                print("You pick up a necklace, and place it around your neck.")
                game.inventorys.append("necklace")
                game.logic()
            else:
                print("You already have a necklace.")

    def pickupmatchbox():
        print(game.matchbox)
        print("You pick up the matchbox, and have a look inside. The matchbox only has 3 matches, and the striking surface appears heavily used.")
        game.inventorys.append("matchbox")
        game.logic()

    def usenecklace():
        print(game.necklace)
        print("You can't think of a use for your necklace.")
        game.logic()    

    def usematchbox()
            print(game.matchbox)
            print("You don't want to waste any matches.")
            game.logic()
    # Game intro
    def l1game():
        #plain text for an introduction to the scene, used for cansee = 0
        print("You wake on the cold dirt, gasping for air, with the only one you muster leaving a thick layer of dust in your mouth.")
        print('')
        time.sleep(2)
        print("It's freezing cold, the only noise you hear are distant crickets and the trees swaying side-to-side as they are caught by the wind.")
        print('')
        time.sleep(2)
        if game.cansee == 0:
            print("You can't see anything.")
            print('')
            print("You run your hand across the ground and find a stick, a necklace and a matchbox.")
        elif cansee == 1:
            print("You see some of the area around you. It's dark, but you can see the faint outline of trees, as well as a few objects on the ground.")
            print('')
            print("You run your hand across the ground and find a stick, a spoon, a necklace and a matchbox.")

        elif cansee == 2:
            print(game.cansee) 
        time.sleep(2)
        game.logic()
    

    def logic():
        global choiceg
        choice = input(">> ")
        choiceg = choice
        if 'crag' in choice:
            print(game.crag)
            game.logic()
        if 'look crag' in choice:
            game.lookall()
        if 'exit' in choice:
            game.exit()
        if 'look all' in choice:
            game.lookall()
        if 'look necklace' in choice:
            game.lookall()
        if 'look stick' in choice:
            game.lookall()
        if 'inventory' in choice:
            game.inventory()
        if 'pick-up stick' in choice:
            game.pickupall()
        if 'pick-up spoon' in choice:
            game.pickupall()
        if 'look spoon' in choice:
            game.lookall()
        if 'look necklace' in choice:
            game.lookall()
        if 'look matchbox' in choice:
            game.lookall()
        if 'pick-up necklace' in choice:
            game.pickupall()
        if 'pick-up matchbox' in choice:
            game.pickupall()
        if 'use stick' in choice:
            game.usestickall()
        if 'use spoon' in choice:
            game.usespoonall()   
        if 'use necklace' in choice:
            game.usenecklace()
        if 'use matchbox' in choice:
            game.usematchbox()
        if 'pickup' in choice:
            print('look, i know you are testing this. just dont.') 
            game.logic()    
        else:
            print("I didn't understand what you meant. Try again.")
            game.logic()

class l2game:
    def l2game():
        print("churchnigga")

    time.sleep(2)
setup.startup()

"""
- Wake up in cage
- Get out of cage
- Find self in woods
- Walk around woods - lots of cereal(crunchy) leaves
- Hear noises (possibly running footsteps(creating more cereal noises) or growls)
- Find abandoned church
- Explore church - find lockpicks, keys, knife.
- Find bodybags
- Hear keys jingling, somebody trying to unlock a door
- Try run from church
- Trip on a divot, and fall into a trap
- KO
- Wake up in church hung upside down amongst the bodybags
- Use knife to cut rope that you're being hung by - Give option to pick up rope
- Sneak out of church, avoiding the CRAG - official name btw "CRAG"
- Find beheading axe out back of church - pick that shit up fam
- Hear people yelling and screaming 
- Door behind you opens
- Piss bolt out of church - give player options to hide (behind a tree, nearby shed, river bank etc.)
    - Time based - countdown
        - Behind tree doesn't work, forced to find somewhere else 
        - Cut self on something in shed, have to find something to stop the bleeding
        - Completely safe on river bank
- Find a nearby outhouse, maybe they have something to stop bleeding - or to pick up
- Enter outhouse
- Completely empty
- Go outside and find CRAGS with lanterns walking around
- Stay in outhouse for a while
- Find a basement
- Enter basement
- Find shit tonnes of supplies, including a bandage, but cut self on way down forcing to use 2 bandages if already cut from shed.
    - You don't have 2 bandages retard
- Other supplies include:
    - Fire for warmth
    - Food
    - Water
    - A bed
- Sleep in basement for night
- Wake up to CRAGS taking you somewhere, you're completely stripped bare, they took everything 
- You can choose to:
    - Run
    - Stay and let them do whatever
    - Yell at them to negotiate
- Nothing works - forced to let the CRAGS do whatever
    - Running ends up in them catching you, never works
    - They don't speak any English so negotiating won't work
- They take you to the church again 
- A ritual is being set up 
    - You're getting sacrificed
- Try to run out of church, works, but they end up catching you
- Try to run again and find the cage where you initially woke up
- Daylight breaks (coincidence amirite)
- If bandage used - die
- If not: 
    - You see a switch, couldn't see it before
    - Give choice of flicking switch
        - If yes: clear all text (if you can do that) and end game 
        - If no: clear all text (again, if you can do that) and restart game, forcing player to go through it all to complete

If yes: give achievement: The easy way out
If no: give achievement: A real competitor

Scroll credits

The end :)
"""

#items needed for level 2
"""
Items:
- Axe
- Rope
- Lockpick
- Keys
- Bandage
- Knife

Options for hiding:
- Behind tree - They find you, forcing you to hide elsewhere
- Behind nearby shed - Works, but you cut yourself trying to hide, forcing you to use a bandage 
- Nearby river bank - best option

"""
#make sure to give more options to pick stuff up during rest of story.