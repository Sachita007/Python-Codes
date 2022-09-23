import random
import os
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
def cheack_ace(list):
    if 11 in list and sum_card(list)>21 :
        list.remove(11)
        list.append(1)

def sum_card (list=[]):
    
    sum_list=0
    for i in list:
        sum_list+=i
    return sum_list
def select (list=[]):
    num=random.choice(list)
    return num
def wining_cheak(list1=[],list2=[]):
   

    if sum_card(list1)==21 and len(list1)==2:
        return "You have blackjack. You win"
    elif sum_card(list2)==21 and len(list2)==2:
        return "Openent have blackjack. You lose"
    elif sum_card(list1)>sum_card(list2):
        if sum_card(list1)>21:
            return "You went over. You lose"
        else:
            return "Yow win"
    elif sum_card(list1)<sum_card(list2):
        if sum_card(list2)>21:
            return "Oppent went over. You win "
        else:
            return "You lose"
def comp_pick(list1=[],list2=[]):
    

    sum_of_card_17_and_more=False
    while not sum_of_card_17_and_more:
        list1.append(select(list2))
        if sum_card(list1)>=17:
            sum_of_card_17_and_more=True



def game_start():
    
    print(logo)
    p_num=[]
    c_num=[]
    to_play=input("Do yo want to play a game of Blackjack? Type 'y' or 'n'.").lower()
    if to_play=="y":
        p_num.append(select(cards))
        p_num.append(select(cards))
        c_num.append(select(cards))
        def game():
            print(f"Your cards: {p_num}, and your score:{sum_card(p_num)}.\nComputer's 1st card: {c_num[0]}")
            a_card=input("Type 'y' to get another card,type 'n' to pass.").lower()
            if a_card=="n":
                #sum_of_card_17_and_more=False
                #while not sum_of_card_17_and_more:
                #    c_num.append(select(cards))
                #    if sum_card(c_num)>=17:
                #        sum_of_card_17_and_more=True
                comp_pick(c_num,cards)
                cheack_ace(p_num)
                cheack_ace(c_num)
                print(f"Your final hand:{p_num}, Final score :{sum_card(p_num)}\nComputer's final hand: {c_num}, Final score: {sum_card(c_num)}")
                print(f"{wining_cheak(p_num,c_num)}")
                game_start()
                
            elif a_card=="y":
                p_num.append(select(cards))
                if sum_card(p_num)>21:
                    comp_pick(c_num,cards)
                    cheack_ace(p_num)
                    cheack_ace(c_num)
                    print(f"Your final hand:{p_num}, Final score :{sum_card(p_num)}\nComputer's final hand: {c_num}, Final score: {sum_card(c_num)}")

                    print(f"{wining_cheak(p_num,c_num)}")
                    game_start()
                    
                game()
        game()
game_start()