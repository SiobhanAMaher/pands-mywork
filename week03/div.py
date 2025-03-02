#div.py
#programme that reads in two numbers and divides the first one by the second and gives the interger result and the remained
#author: Siobhán Maher

x = int (input("Enter first number: "))
y = int (input("Enter the number you want to divide by: "))
answer = int(x / y)
remainder = x%y

print (" {} divided by {} is {} with remainder {} ".format(x, y, answer, remainder))