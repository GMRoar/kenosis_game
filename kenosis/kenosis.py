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
           print('Nate has a fat belly')
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
        

