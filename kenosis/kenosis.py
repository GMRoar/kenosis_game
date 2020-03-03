import time
class setup:
    
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
        if 'y' in playTutorial:
            tutorial.tutorialintro()
        if 'Y' in playTutorial:
            tutorial.tutorialintro()
        else:
            game.l1intro()

class tutorial:
    #Variables required for inventory.
    coins = 0
    
    # Look commands.
    def endtutorial():
        print("Starting Kenosis...")
        time.sleep(2)
        game.l1intro()
    def where():
        tutorial.tutorialintro()
    def usecoins():
        if coins == 1:
            print("You throw the coins across the room.")
            coins = 0
        time.sleep(1)
        tutorial.tutorialroom()
    def looksign():
        print("You look at the sign. The sign reads: 'Tutorial'.")
        time.sleep(1)
        tutorial.tutorialroom()
    def lookall():
        print("You look at your surroundings. You see: sign, chair, table, window.")
        time.sleep(1)
        tutorial.tutorialroom()
    def lookchair():
        print("You inspect the chair. It's just a wooden chair. It's starting to decay from rot.")
        time.sleep(1)
        tutorial.tutorialroom()
    def looktable():
        print("You inspect the table. It's just a wooden table. It's starting to decay from rot.")
        time.sleep(1)
        tutorial.tutorialroom()
    def lookwindow():
        print("You look out the window. It's pitch black, you can't see anything.")
        tutorial.tutorialroom()
    # Pick-up commands.
    def pickupcoins():
        print("You pick-up the coins, and place them in your pocket.")
        tutorial.coins = 1
        tutorial.tutorialroom()

    #Use commands.



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
            time.sleep(1)
            print("You awake in a dark room. Ahead is a wall, with a bright neon sign hanging on it. There is also a table, chair, window and some coins on the floor.")
            print("")
            time.sleep(1)
            print("Welcome to the tutorial. You can test the various commands that you will use in Kenosis to navigate, interact and inspect.")
            print("")
            time.sleep(1)
            print("These commands are: look, pick-up, where, inventory.")
            print("")
            time.sleep(1)
            print("The 'look' command let's you look at an object, or all objects. First try 'look all' to list all objects in a room, then 'look (obj)' to inspect it.")
            print("")
            time.sleep(1)
            print("The 'pick-up' command allows you to pick up an object. This will only happen on objects you can pick up though. Try 'pick-up (obj)'.")
            print("")
            time.sleep(1)
            print("The 'where' command repeats the scene opening, such as the 'Ahead is a wall, with a ...' at the start of this tutorial. Try 'where'.")
            print("")
            time.sleep(1)
            print("The 'inventory' command lists all items you have picked up. Try 'inventory'.")
            print("")
            time.sleep(1)
            print("The 'use' command allows you to use an object you have in your inventory. Try 'use (obj).")
            print("")
            time.sleep(1)
            print("Note: All commands are in lower-case.")
            print("")
            time.sleep(3)
            print("Try any of these commands in this tutorial sequence. When you are finished, type 'end tutorial'.")
            print("")
            tutorial.tutorialroom()       



    
    def tutorialroom():
        #var
        choice = input(">> ")
        #game routine
        if 'look sign' in choice:
            tutorial.looksign()
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
        else:
            print("I didn't understand what you meant. Try again.")
            tutorial.tutorialroom()

class game:
    #Inventory Variables
    inventorys = {"spoon":1,"stick":1,"necklace":1}

      # Inventory
    def inventory():
         for key, value in game.inventorys.items():
            if value == 1:
                print("You check your pockets, and find:", key)
                time.sleep(1)
                game.logic
            if value != 1:
                print("You find nothing in your pockets.")
                time.sleep(1)
                game.logic
  
    
    
    
    
    
    
    #Art
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
    #Defines use commands
    def usestick():
        print("You try to pry at the bars with the stick, but the stick is too thin and breaks before any bars are bent")
        if "stick" in choice:
            time.sleep(2)
            store.usestick()

    def usespoonlock():
        print("You use the spoon on the lock. With a bit of time, you manage to pick the lock,")


    def usecrucifix():
         print("The crucifix might be useful later, let's not use it here.")
         if "crucifix" in choice:
             store.usecrucifix()
    #Defines look commands
    def lookall():
        print("You feel around on the ground. You feel a few objects on the ground that feel like a stick, a spoon and a necklace.")
        game.logic()

    def looknecklace():
        print(game.necklace)
        print("You look at the necklace. It is made of a thin, linked chain and a wooden crucifix hanging off it.")
        game.logic()

    def lookstick():
        print(game.stick)
        print("You look at the stick. It's a stick.")
    #Defines pick-up commands
    def pickupstick():
        print(game.stick)
        print("You pick up the stick, and put it in your pocket.")
        game.inventorys["stick"] = 1
        game.logic()

        

    # Game intro
    def l1intro():
        #plain text for an introduction to the scene
        print("You wake on the cold dirt, gasping for air, with the only one you muster leaving a thick layer of dust in your mouth.")
        print("It's freezing cold, the only noise you hear are distant crickets and the trees swaying side-to-side as they are caught by the wind.")
        print("You can't see anything.")
        time.sleep(2)
        game.logic()
       #"You feel around for your glasses, with no luck, but you do find a what feels to be a stick, a spoon, and a crucifix on the ground." 
        # print("Crucifix Acquired!")
       # print("Upon walking around, you discover that you're locked in a small cage, possibly for chickens. Some of the bars are bent, but you're not strong enough to break them")
     
       # Game Logic
       
    def logic():
        choice = input(">> ")
        if 'look all' in choice:
            game.lookall()
        if 'look necklace' in choice:
            game.looknecklace()
        if 'look stick' in choice:
            game.lookstick()
        if 'look spoon' in choice:
            game.lookspoon()
        if 'inventory' in choice:
            game.inventory()
        if 'pick-up stick' in choice:
            game.pickupstick()
        if 'pick-up spoon' in choice:
            game.pickupspoon()
        if 'pick-up necklace' in choice:
            game.pickupnecklace()
        if 'pick-up matchbox' in choice:
            game.pickupmatchbox()

class Game:
    def challenge(): 
        #First user challenge
        print("Here are your options:")
        time.sleep(2)
        #Option A
        print("Will you: Try to pry the cage open with the stick")
        #Option B
        print("Will you: Dig a hole underneath the cage with the spoon")
        #Option C
        print("Will you: Use the crucifix to pry the cage open")
        #Asks user for choice
        choice = input("What will you choose? ")

    time.sleep(2)
setup.startup()


