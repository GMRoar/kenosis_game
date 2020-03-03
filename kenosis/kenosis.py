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
            game()

class tutorial:
    #Variables required for inventory.
    coins = 0
    
    # Look commands.
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
            time.sleep(1)
            print("You awake in a dark room. Ahead is a wall, with a bright neon sign hanging on it. There is also a table, chair, window and some coins on the floor.")
            print("Welcome to the tutorial. You can test the various commands that you will use in Kenosis to navigate, interact and inspect.")
            print("These commands are: look, pick-up, where, inventory.")
            print("The 'look' command let's you look at an object, or all objects. First try 'look all' to list all objects in a room, then 'look (obj)' to inspect it.")
            print("The 'pick-up' command allows you to pick up an object. This will only happen on objects you can pick up though. Try 'pick-up (obj)'.")
            print("The 'where' command repeats the scene opening, such as the 'Ahead is a wall, with a ...' at the start of this tutorial. Try 'where'.")
            print("The 'inventory' command lists all items you have picked up. Try 'inventory'.")
            print("The 'use' command allows you to use an object you have in your inventory. Try 'use (obj).")
            print("Note: All commands are in lower-case.")
            time.sleep(5)
            print("Try any of these commands in this tutorial sequence. When you are finished, type 'end tutorial'.")
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
        if 'inventory' in choice:
            tutorial.inventory()
        else:
            print("I didn't understand what you meant. Try again.")
            tutorial.tutorialroom()
class game:
    time.sleep(2)
setup.startup()


