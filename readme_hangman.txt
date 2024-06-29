# Step 1
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO 1 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#Create an empty list called display.
#create a variable called 'lives' to keep track of the number of lives left.
#set 'lives' to equal 6
#or we can use the below code

# display = []
# for letter in chosen_word:
#     display += "-"
# print(display)

#for each letter in the chosen_word, add a "_" to "display".
#So if the chosen_word was "apple" , display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

    #TODO 2 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #if the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #eg: If the user guessed "p" and the chosen_word was "apple" , then display should be ["_", "p", "p", "_", "_"].
    # If guess is not a letter in the chosen_word.
#then reduce 'lives' by 1.
#if lives goes down to 0 then the game should stop and it should print "You lose"
  #TODO 3 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.