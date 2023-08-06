# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 00:51:27 2023

@author: Nabanita Paul
"""

# number guessing 

import random
import math

lower_boundary = int(input("Enter a lower Boundary: "))
upper_boundary =int(input("Enter a upper Boundary: "))

no_of_chances = round(math.log(upper_boundary-lower_boundary +1,2))

print("You have only {} chances remaining".format(no_of_chances))

count=0
x= random.randint(lower_boundary,upper_boundary)


while count< round(math.log(upper_boundary-lower_boundary +1,2)):
    count=count+1
    guess = int(input("Guess a number: "))
    if x<guess:
        print("You guess too high")
    elif x>guess:
        print("You guess too low")
    elif x==guess:
         print("You guessed correctly")
         break
if count  >= round(math.log(upper_boundary-lower_boundary +1,2)):
    print("The number is {}".format(x))
    print("Better Luck next time")
