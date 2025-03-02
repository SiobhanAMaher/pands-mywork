#isEven.py
#Write a program (isEven.py) that asks the user to enter in a number, and the program will tell the user if the number is even or odd. 
#Author: Siobhán Maher

number=int(input("enter a number:"))
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print (f"{number} is an odd number")