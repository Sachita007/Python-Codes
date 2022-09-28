from game_data import data
import random
from art import logo, vs
from os import name, system


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


# --Function to chose random account
def chose_data(data):
    dict = random.choice(data)
    return dict


# --Function to check the guess is correct or not
def check_score(guess, compare, against):
    if guess == "a":
        return compare['follower_count'] > against['follower_count']

    elif guess == "b":
        return compare['follower_count'] < against['follower_count']


print(logo)
compare = chose_data(data)  # --Chosing first account(account to compare)
game_should_continue = True  # --Creating the flag for while loop
score = 0  # --Defining the score

while game_should_continue:

    # --Printing the first account data
    print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")

    against = chose_data(data)  # --Choosing second account (account on against)
    if against == compare:  # --Checking if both choosen acount is same or not if same change account
        against = chose_data(data)

    print(vs)  # --Printing logo

    # --Printing second accout data
    print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()  # --Asking for guess
    clear()  # clearing the screen
    print(logo)
    guess_cheack = check_score(guess, compare, against)  # --Cheacking the score
    if guess_cheack:
        score += 1
        print(f"You're right! Final score:{score}")

        compare = against  # --If correct changing  the position of second account to first ,and choosing random for second
    else:
        print(f"Sorry that's wrong.Final score:{score}")
        game_should_continue = False

        # -----Previous Code------#

    # if follower_guess=="a":
    #    if compare['follower_count']>against['follower_count']:
    #        score+=1
    #        compare=against
    #        print(f"You're right! Final score:{score}")
    #        
    #    else:
    #        game_should_continue=False
    # elif follower_guess=="b":
    #    if compare['follower_count']<against['follower_count']:
    #        score+=1
    #        compare=against
    #        print(f"You're right! Final score:{score}")
    #    else:
    #        game_should_continue=False
# print(f"Sorry that's wrong.Final score:{score}")
