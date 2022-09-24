#----Importing Modules

import hangman_art
import hangman_word_list
import random
import os
print(hangman_art.logo)

'''TODO-1 - Randomly choose a word from the word_list 
and assign it to a variable called chosen_word.'''


chose_random=random.choice(hangman_word_list.word_list)
number_of_letters=len(chose_random)    #counting the number of letters in random word
list_letters=[]                        #creating list for the random word.

'''filling the list with blanks'''
for i in chose_random:
    list_letters+="_"
w=len(chose_random)
at_goal=False
k=6 #---lives
#Entering the for loops upto range w(number of letters in random word)+  3 extra wrong attempt
while not at_goal:

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  
  
    guess=input("Guess a letter:\n").lower()

    os.system('cls')

    x=chose_random.count(guess)    #counting the how many time guessed letters is comming
    
    if x==0:                          #|  cheacking is the user guessed a correct letter  or not
          
        print("You guessed a wrong word and you loose a life.")                        
        k-=1                           
    if k==0:                       #|    if user guessed incorrect more then three time exit the loop
        at_goal=True       


    elif x>0:       
        
        if guess in list_letters:
                    print(f"You already guessed {guess}.")     
        #---entring the loop for replacing the blanks with guessed word


        for i in range(w):
            letter=chose_random[i]


             
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
                    
            if guess==letter:  
                   
                list_letters[i]=guess
    print(f"{''.join(list_letters)}")
    if "".join(list_letters)==chose_random: #--cheacking is the word is completed or not
        at_goal=True     
    print(hangman_art.stages[k])            
    
if k==0:
    print("You loose") 
else:
    print("You Win!")           