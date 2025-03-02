#grademod2.py
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
#How would you use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1 
#Author: Siobhán Maher


val = int(input("Enter minus 1: "))
if val == -1:
    print("Thank you for entering minus 1")
while val != -1:
     print ("Please enter minus 1: ")
     val = input ("Enter minus 1!!!!")
     if val == -1:
        print("Thank you for entering minus 1")
    
