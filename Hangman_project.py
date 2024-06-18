# Step 1

word_list = ["ardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)
#TODO 1 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#Create an empty list called display.

display = []
for _ in range(word_length):
    display += "-"
print(display)

#or we can use the below code

# display = []
# for letter in chosen_word:
#     display += "-"
# print(display)

#for each letter in the chosen_word, add a "_" to "display".
#So if the chosen_word was "apple" , display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess = input("Guess a letter:")
#TODO 2 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#if the letter at that position matches 'guess' then reveal that letter in the display at that position.
#eg: If the user guessed "p" and the chosen_word was "apple" , then display should be ["_", "p", "p", "_", "_"].
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO 3 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


