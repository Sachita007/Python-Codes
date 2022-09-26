import os
from art import logo
print(logo)
print("Welcome to secret auction programe .")
name_and_bid={}     # creating empty dictinoary
end=False                
while not end:      # entring into while loop and continues till "end" is false
    
    name=input("What is your name? :")                 # tasking for name of bidder 
    bid=int(input("What's your bid? : $"))             # Asking for his bid
    name_and_bid[name]=bid                       #--Adding the name and bid in dictinoary
    os.system('cls') #--it used for cleaning the screen after each loop
    any_other=input("Are there is any other bidders? Type 'yes' or 'no'." ).lower()  
    if any_other=="no":          # if there is no bidder ending the loop
        end=True

max_bid=0
person="any"
for bidder in name_and_bid:  # for each key in dictionary in entring for loop For finding maximum bid
    amount=name_and_bid[bidder]  # accesing kry's value
    if amount>max_bid:            
        max_bid=amount             
        person=bidder
print(f"The winner is {person}, with highest bid ${max_bid}.")