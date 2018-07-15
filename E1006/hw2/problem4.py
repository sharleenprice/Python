#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:37:38 2017

@author: sharleenprice spp2122
"""


def select_meal():
    vars = True
    order = ""
    counter = 0
    while(vars):
        meal = input("Hello, would you like pizza or salad? " )
        if counter <1:
            if meal == "pizza":
                order= pizza()
            elif meal == "salad":
                order = salad()
            elif meal == "done":
                vars = False
                break
            else:
                continue
        else:
            if meal == "pizza":
                order+= " and a {}".format(pizza())
            elif meal == "salad":
                order += " and a {}".format(salad())
            elif meal == "done":
                vars = False
                break
            else:
                continue
        
        print("\nYou ordered a {} \nPlace another order or say  done'. ".format(order))
        counter += 1
        
    print()
    print("Your order has been placed, goodbye")
    


def pizza():
    size = input("Small, Medium, or Large? ")
    return "{} pizza{}".format(size,toppings())

def toppings():
    counter = 0
    vars = True
    top = ""
    while(vars):
        topping = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'.  ")
        if counter<1:
            if (topping == "done"):
                break
            else:
                top += " with {}".format(topping)
                counter +=1
        else:
            if (topping == "done"):
                break
            else:
                top += " and {}".format(topping)
    return top


def salad():
    salad = input("Would you like a garden or greek salad? ")
    return "{} salad with {} dressing".format(salad, dressing())

def dressing():
    dressing = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon  ")
    return dressing

select_meal()