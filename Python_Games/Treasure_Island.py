#('''_______''') used because this string has many lines .
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
cross_road=input("You are atcros road. Where do yoy want to go? Type 'left' or 'right'?\n")
if cross_road=='left' or cross_road=='Left':
    came_to_lake=input("You came to lake. There is an island inthe middle of the lake. Type 'wait' to wait for boat or Type 'swim' to swim across\n")
    if came_to_lake=='wait' or came_to_lake=='Wait':
        island=input("You arrived at the island unarmed.There is a house with 3 doors. One red, one blue, and one yellow. Which colour do you Choose?\n")
        if island=='yellow' or island=='Yellow':
            print("You Win!")
        elif island=='blue' or island=='Blue':
            print("Eaten by beast.\nGame Over.")
        elif island=='red' or island=='Red':
            print("Burned by fire.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout\nGame Over.")
else:
    print("Fall into hole.\nGame Over")        