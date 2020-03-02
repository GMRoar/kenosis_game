intro = """

 _        _______  _        _______  _______ _________ _______ 
| \    /\(  ____ \( (    /|(  ___  )(  ____ \\__   __/(  ____ \.
|  \  / /| (    \/|  \  ( || (   ) || (    \/   ) (   | (    \/
|  (_/ / | (__    |   \ | || |   | || (_____    | |   | (_____ 
|   _ (  |  __)   | (\ \) || |   | |(_____  )   | |   (_____  )
|  ( \ \ | (      | | \   || |   | |      ) |   | |         ) |
|  /  \ \| (____/\| )  \  || (___) |/\____) |___) (___/\____) |
|_/    \/(_______/|/    )_)(_______)\_______)\_______/\_______)
                                                               
(C) Nathanial Landers & Leyton Frecklington 2020.

"""
print(intro)
tutw = None
choice = None
class tutorial:
    tutw = input("Would you like to play the tutorial (recommended)? (Y/N): ")
if tutw == 'Y':
    print("Starting Tutorial...")
    print("You awake in a dark room. You see a bright neon sign in the distance.")
choice = input("To interact with your environment, you must use various commands. Please type 'look sign' to proceed.")
else:
        exit
elif choice == 'look sign':
    print("You read the neon sign. It reads 'Tutorial'.")
else:
    print("Please type 'look sign'.")

