print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ____...------------...____
      _.-"` /o/__ ____ __ __  __ \o\_`"-._
    .'     / /                    \ \     '.
    |=====/o/======================\o\=====|
    |____/_/________..____..________\_\____|
    /   _/ \_     <_o#\__/#o_>     _/ \_   \
    \________________\####/________________/
     |===\!/========================\!/===|
     |   |=|          .---.         |=|   |
     |===|o|=========/     \========|o|===|
     |   | |         \() ()/        | |   |
     |===|o|======{'-.) A (.-'}=====|o|===|
     | __/ \__     '-.\\_//.-'    __/ \__ |
    _|==== .o|o.=================.o|o. ====|_
   /  """""""""""""""""""""""""""""""""""""\ 
  /  -= TREASURE =- -= CHEST =- -= FILLED =- \
 /_____________________________________________\
'-----------------------------------------------'

""")
print("Welcome to Treasure Island")
print("Your mission is to find the treasures.")
choice1 = input("You're at a crossroad, where do you want to go? Type left or right." ).lower()

if choice1 == "right":
#Game will continue
    choice2 = input(" \n You are come to a lake. There is an island in the middle of the lake . Type wait to wait for a boat. Type swim to swim across.\n").lower()
    if choice2 == "wait":
#Game will continue
        choice3 = input("\n You arrive at the island Unharmed. There is a house with 3 doors. One red , One Yellow and One blue.Which color do you choose?\n").lower()
        if choice3 == "red":
            print("\n It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("\n You found the treasure ! You win!")
        else:
            print("\n You enter a room of beasts. Game Over.")


    else:
        print("You got attacked by an angry trout. Game Over!")

else:
    print("You fell into a hole. Game Over.")




