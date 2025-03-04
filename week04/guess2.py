#guess2.py
#Write a program (guess2.py) that prompts the user to guess a number, the program should keep
#How would you modify the program in 3 (guess2.py) above, so that the 
#program tells the user if there guess is too high or too low, each time they
#guess. HINT: put an  if statement inside the while loop 
#Author: Siobhán Maher

import random 

numberToGuess = random.randint(1, 100)
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too Low!")
    else: 
        print("Too high!")
    guess = int(input ("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)