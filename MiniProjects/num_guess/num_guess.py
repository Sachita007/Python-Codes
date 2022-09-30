import random
import os
from art import logo

    
#--game function so we can call and restrart the game
def game(): 
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    dificulty=input("Chose adificulty. Type 'easy' or 'hard': ").lower()  
    n=0
    k=0
    if dificulty=="easy":
        n=10  #--Attempts
    elif dificulty=="hard":
        n=5  #--Attempts
    c_guess=random.randint(1,100)  #--Computer random guessed number 
    for i in range (0,n):
        k+=1
        print(f"You have {n-i} attemps remainig to guess the number.")
        guess=int(input("Make a guss: "))       #--User guessed number
        if guess==c_guess:                                  
            print(f"You got it! The number is {guess}")        
            break                                                          
        elif guess<c_guess:
            print("Too low.")
            if n-i==1:
                break
            print("Guess Again.")
        elif guess>c_guess:
            print("Too High.")
            if n-i==0:
                break
            print("Guess Again.")
    if k==n:
        print("You've run out of guss, you lose.")
    paly_again=input("Do you want to play again.Type 'yes' or 'no'.")
    if paly_again=='yes':
        os.system('cls')
        game()
game()   


