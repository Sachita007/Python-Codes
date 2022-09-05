# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#converting all upper case letter in lower case in both name
name1a=name1.casefold()
name2a=name2.casefold()
#using variable x and y for counting letter specific letter in both name 
x=0
y=0

# counting the letters from 'True', in both name
x=x+(name1a.count("t"))+(name2a.count("t"))
x=x+(name1a.count("r"))+(name2a.count("r"))
x=x+(name1a.count("u"))+(name2a.count("u"))
x=x+(name1a.count("e"))+(name2a.count("e"))

# counting the letters from 'LOVE', in both name
y=y+(name1a.count("l"))+(name2a.count("l"))
y=y+(name1a.count("o"))+(name2a.count("o"))
y=y+(name1a.count("v"))+(name2a.count("v"))
y=y+(name1a.count("e"))+(name2a.count("e"))

#we got x and y in integer, so we conver it into string.
str1=str(x)
str2=str(y)

#combining string and converting it to integer
score=int(str1+str2)

#cheacking conditions
if score<10 or score>90:
    print(f"Your score is {score},you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")