# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 4.16: Largest Number
# Date:         8 September 2023

#asks for numbers
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

if (num2 > num1):                   #route if num2 is greater than num1
    largestnum = num2
    if (num2 > num3):
        largestnum = num2
    elif (num3 > num2):
        largestnum = num3
elif (num1 > num2):                 #route if num1 is greater than num2
    largestnum = num1
    if (num1 > num3):
        largestnum = num1
    elif (num3 > num1):
        largestnum = num3

print("The largest number is", largestnum)
