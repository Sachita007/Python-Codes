import os

#--Add
def add(n1,n2):
    return n1+n2

#---Sunbtract
def sub(n1,n2):
    return n1-n2

#---Devide
def devide(n1,n2):
    return n1/n2

#--Multiply
def multiply(n1,n2):
    return n1*n2

    #--Creating Dictionary for different operation for easy assesing the operations
operation = {
    "+":add,
    "\\":devide,
    "-":sub,
    "*":multiply,

}

def calculator():
    """ To perform Mathematical operation (Calculator)"""
    from art import logo   #importinf logo from art file
    print(logo)
    num1=float(input("What's the first number? ")) # Taking input 
    for symbol in operation:         #Printing symbol by using Dictionary created before
        print(symbol)
    should_continue=True           # Creating flag for while loop 
    while should_continue:
        operation_symbol=input("Pick an operation.")     # Asking for operation from perform
        num2=float(input("What's the second number? "))  
        
        function=operation[operation_symbol] # calling function of operations
        answer=function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")     # printing output
        further_operation=input(f"Type 'y' calculate with {answer} ,or type 'n' to restart the calculation. ") # Asking fro continue and exit
        if further_operation=="y":
            num1=answer
        elif further_operation=="n":
            should_continue=False
            os.system('cls')
            calculator()  # Finction Calling itself (Recursion)

#Calling Function
calculator()
    
        
    