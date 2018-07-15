#/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:38:32 2017

@author: sharleen price spp2122
"""
import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}{}".format(self.suit,self.rank)
        # replace this line

    def value(self, total):
        try:
            num_rank = int(self.rank)
            return num_rank
        except ValueError:
            if(self.rank == "A"):
                if (int(total)+11>21):
                    return 1
                else:
                    return 11
            else:
                return 10 

def make_deck():

    suits = ['♠','♣','♦','♥']
    deck = []
    for i in range(4):
        for j in range(2,11): #integer cards
            card = Card(suits[i],str(j))
            deck.append(card)
        card = Card(suits[i], "J") #facevalue cards
        deck.append(card)
        card = Card(suits[i], "Q")
        deck.append(card)
        card = Card(suits[i], "K")
        deck.append(card)
        card = Card(suits[i], "A")
        deck.append(card)
    
    random.shuffle(deck)
    return(deck)
    

def main():
    deck = make_deck()
    user_sum = 0
    user_input = "y"
    
    
    while(user_input == "y" and user_sum<21):
        print("You drew a {} ".format(deck[0].__str__()))
        user_sum += deck[0].value(user_sum)
        print("Sum: {}".format(user_sum))
        del deck[0]
        if user_sum > 21:
            print("You Lost")
            break
        elif user_sum == 21:
            print("You Win!")
            break
        user_input = input("Do you want another card? (y/n) ")
    
        
    if(user_sum<21):
        comp_sum = 0
        while(comp_sum < 17):
            print("I drew a {} ".format(deck[0].__str__()))
            comp_sum += deck[0].value(comp_sum)
            print("Sum: {}".format(comp_sum))
            del deck[0]
        if comp_sum > 21:
            print("I lost, You Win.")
        elif comp_sum == 21:
            print("I Win!")
            
    if(user_sum<21 and comp_sum <21):
        if (user_sum == comp_sum):
            print("Push")
        elif(user_sum>comp_sum):
            print("You Win!")
        elif(user_sum<comp_sum):
            print("I win!")

if __name__ == "__main__":
    main()
