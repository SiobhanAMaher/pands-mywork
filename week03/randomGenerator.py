#RandomGenerator.py
#program that prints out a random number between 1 and 10
#author: Siobhán Maher

import random

from random import randrange


number = randrange (1,100)
print ("Select two numbers, a min and a max")
a = int(input("Select min: "))
b = int(input("Select max: "))

print(randrange(a,b))
