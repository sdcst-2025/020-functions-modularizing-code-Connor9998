"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
import math

x=random. randint(1, 10)

def title():
    print("Guesse a number between 1 and 10, good luck!")

def game():
    w=print (input("Enter your guesse for a number between 1 and 10: "))
    while x != w:
        w=print (input("Enter your guesse for a number between 1 and 10: "))
        if (f"int(w) == x"):
            print("correct")
            break
            
        

title()


game()

    
