#!/usr/bin/env python3


import random
import os

def main(userInput):
    userInput = int(userInput)
    if userInput < 1000 and userInput > 1:
        guess = random.randint(0,1000)    
        for i in range(1000):
            while guess != userInput:
                if userInput > guess:   # if the guess was too small:
                    guess = random.randint(guess, 1000)
                    print(f"guess: ",guess, "is lower")
                elif userInput < guess: # if the guess is too big
                    guess = random.randint(1, guess)
                    print(f"guess: ",guess, "is higher")

userInput = input("pick a number between 1 - 1000:  ")
if userInput == "":
    print("[Error need user input!!!]")
else: 
    
    main(userInput)



   
                    
            
           


