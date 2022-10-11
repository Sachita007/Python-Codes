import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images=[rock, paper, scissors]  #included the images in list in order.
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")) #Taking user input.

if choose>2:
    print("You typed an invalid number!")   
   
else:
  print(game_images[choose]) #Printing images crrosponding to user input
  computer=random.randint(0,2)     #Choosing computer's random choice


  print("Computer chose:")
  print(game_images[computer])  #printing image of computer's choice.
  
  if computer==0 and choose==1:
      print("You Win")
  elif computer==1 and choose==2:
      print("You Win")
  elif computer==choose:
      print("Draw")
  
  else:
      print("You lose")
