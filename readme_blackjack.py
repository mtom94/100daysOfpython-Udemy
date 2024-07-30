#Hint 4 : Create a deal_card() function that uses the list below to *return* a random card.
#11 is the Ace

#Hint 5 : Deal the user and computer 2 cards each using deal_card()
#user_cards []
#computer_cards = []

#Hint 6 : Create a function called calculate_score() that takes a List of cards as input
#and returns the score
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack(a hand with only 2 cards: ace + 10)
#and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8 : Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append () and remove()

#Hint 9 : Call calculate_score(). If the computer or the user has a blackjack(0) or if the user's score is over 21, the the game ends.

#Hint 10 : If the game has not ended, ask the user if they want to draw another card. If yes then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.