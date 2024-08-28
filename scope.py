enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")
increase_enemies()
print(f"enemies outside functions: {enemies}")

#Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()

# Global Scope

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)

#There is no Block Scope


game_level = 3
enemies = ["Skelton", "Zombie", "Alien"]

if game_level < 5:
        new_enemy = enemies[0]
print(new_enemy)

# Modifying Global Scope
# In this function we are try to modify the global variable , which is call inside of this function and update the original value (enemies =1).

#we can use the [global] keyword to call the global variable into this function but prone to show some bugs so instead of this we use [return] statements.
enemies = 2
def increase_enemies():
    print(f"enemies inside function : {enemies}")
    #global enemies
    #enemies = +1
    #instead of this we use
    return enemies + 1
enemies= increase_enemies()
print(f"enemies outside functions: {enemies}")

# Global constants
#whenever we use constants in python ,we should be use block letters

PI = 3.14
URL = "http//:google.com"
print(URL)
