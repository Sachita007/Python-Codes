############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from art import logo
import os
def deal_card():       # function for selecting rendom no from list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


    #function for calculating score
def calculate_score(cards):
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    if sum(cards)==21 and len(cards)==2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

    #function cheacking winner by finding score and comparing them
def wining_cheak(user_cards,computer_cards):
    if sum(user_cards) > 21 and sum(computer_cards) > 21:
       return "You went over. You lose 😤"
    if sum(user_cards) == sum(computer_cards):
      return "Draw 🙃"
    elif sum(computer_cards) == 0:
      return "Lose, opponent has Blackjack 😱"
    elif sum(user_cards) == 0:
      return "Win with a Blackjack 😎"  
    elif sum(user_cards)>sum(computer_cards):
        if sum(user_cards)>21:
            return "You went over. You lose 😤"
        else:
            return "Yow win😎"
    elif sum(user_cards)<sum(computer_cards):
        if sum(computer_cards)>21:
            return "Oppent went over. You win😎 "
        else:
            return "You lose😤"

 #function for repeadted asking for play again 
def ask():   
    if input("Do yo want to play a game of Blackjack? Type 'y' or 'n'.").lower()=="y":
        os.system('cls')
        start_game()
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().


def start_game(): #creating funtion for caling it as to restart process
    print(logo)
    user_cards = []         
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())        #| Adding two random num in list from given list of cards 
        computer_cards.append(deal_card())    #| Adding two random num in list from given list of cards 


    def in_game():
        print(f"Your cards: {user_cards}, Final score: {calculate_score(user_cards)}\nComputer's first card: {computer_cards[0]}")
        should_continue=input("Type 'y' to pick another card, 'n' to pass. ") 
        if should_continue=="n":
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
            print(wining_cheak(user_cards,computer_cards))
            ask()  #calling ask function to ask user to play it again
        else:
            user_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            while computer_score != 0 and computer_score < 17:
               computer_cards.append(deal_card())
               computer_score = calculate_score(computer_cards)
            if calculate_score(user_cards)>=21:
               print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
               print(wining_cheak(user_cards,computer_cards))
               ask()
            in_game()  # calling funtion to start form "asking for pick another card aor not"
    in_game() #--Here funtion is called for start asking to pick another 


ask() #--Here ask() called to start the game

# Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 







#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.