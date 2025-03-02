#grademod.py
#Write a program (grade.py) that reads in a student’s percentage mark and 
#prints out corresponding the grade (the program should check that the 
#percentage is valid: 
#Under 40% => Fail 
#Between 40% and 49%  => Pass 
#Between 50% and 59%  => Merit 2 
#Between 60% and 69%  => Merit 1 
#Over 70%    => Distinction 
#In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
#equal to a Distinction.  
#How would you modify the program in 1 to deal with this? 
#Author: Siobhán Maher


percentage = float(input("Enter the percentage: "))
x = round(percentage) # rounds the answer to nearest integer, then use this for printing
if x < 0 or x > 100:
    print ("Please enter a number between 0 and 100")
elif x < 40:
    print("Fail")
elif x < 50:
    print("Pass")
elif x < 60:
    print("Merit 2")
elif x < 70:
    print("Merit 1")
elif x >= 70:
    print("Distinction")