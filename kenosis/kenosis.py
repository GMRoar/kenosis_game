startup = """
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
import time
print(startup)
choice = None
class intro:
    #Defines the lines for looking at the sign.
    def sign():
           print('You read the Neon Sign. The sign reads: "Tutorial".')
           time.sleep(1)
    #Defines the lines for looking at all (in the tutorial).            
    def lookall():
           if choice == "look all":
            print("You look at your surroundings. You see: Sign, Window, Chair.")

    playTutorial = input("Would you like to play the tutorial (Recommended)? (Y/N)")
    lookallf = lookall
    signf = sign
    if playTutorial == 'Y':
            print("Starting Tutorial...")
            time.sleep(2)
            print("You awake in a dark room. Ahead is a wall, with a bright neon sign hanging from it.")
            print("To interact with your environment, you must use a set of commands. First, we will learn the 'look' command.")
            choice = input("To look at the sign, please type 'look sign'. (Note: All commands will be in lower-case.)")
    elif choice == 'look sign':
        sign()
    elif choice != 'look sign':
       ''' print("Please type 'look sign'.")

            choice = input("Good. Now you know how to look at objects and environments in the world. To list all that you can see, type 'look all'.")
            choice = input("Good. Now, if you would like a recap, please type 'recap'. If you would like to move to the next part of the tutorial, type 'next'. You can also look at the other things in your surroundings if you would like.")
            if choice == 'recap':
                print("To recap, to look at an object, type 'look' and the object's name. To list all objects visible, type 'look all'.")
            time.sleep(1)
            sign()
            lookall()
'''
        
"""
choice=input("Now you know how to look at things in the world. To list all that you can see, type 'look all'.")"""
        

class Store:
    #Defines the lines for using the stick
    def usestick():
        print("You try to pry at the bars with the stick, but the stick is too thin and breaks before any bars are bent")
        if "stick" in choice:
            time.sleep(2)
            store.usestick()
    #Defines the lines for using the spoon
    def usespoon():
        print("You dig a big enough hole underneath the base of the cage to crawl out the bottom")
        if "spoon" in choice:
            time.sleep(3)
            store.usespoon()
    #Defines and stores the lines for using the crucifix
    def usecrucifix():
         print("The crucifix might be useful later, let's not use it here.")
         if "crucifix" in choice:
             store.usecrucifix()


class Intro:
    def intro():
        #plain text for an introduction to the scene
        print("You wake on the cold dirt, gasping for air, with the only one you muster leaving a thick layer of dust in your mouth.")
        print("It`s freezing cold, the only noise you hear are distant crickets and the trees swaying side-to-side as they are caught by the wind")
        print("You feel around for your glasses, with no luck, but you do find a what feels to be a stick, a spoon, and a crucifix on the ground")
        time.sleep(2)
        print("Crucifix Acquired!")
        print("Upon walking around, you discover that you're locked in a small cage, possibly for chickens. Some of the bars are bent, but you're not strong enough to break them")
  
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
    