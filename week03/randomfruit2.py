#RandomFruit
#Write a program that prints out a random fruit
#Author: Siobhán Maher

import random
fruits = ('Apple', ' Orange', 'Banana', 'Pear', 'Strawberry', 'Raspberry', 'Lemon')
index = random.randint (0,len(fruits)-1)
fruit = fruits[index]

print ("A Random Fruit: {}".format(fruit))