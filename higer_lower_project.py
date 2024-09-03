from higher_lower_art import logo, logo2
from game_data import higher_lower_data
import random
import os
import platform

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    return (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)

def clear_screen():
    """Clears the screen depending on the OS."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(higher_lower_data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(higher_lower_data)

    while account_a == account_b:
        account_b = random.choice(higher_lower_data)

    print(f"Compare A: {format_data(account_a)}.")
    print(logo2)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear_screen()
    print(logo)

    # Give user feedback on their guess and keep score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
