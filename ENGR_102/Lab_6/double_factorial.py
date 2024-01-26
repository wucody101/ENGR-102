# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 6.14: Double Factorial
# Date:         25 September 2023

def doublefactorial(num):
    amount = 1                              
    if (num % 2 == 0):                                                     #even numbers
        for i in range(2, num + 2, 2):
            amount *= i
    elif (num % 2 == 1):                                                   #odd numbers
        for i in range(1, num + 2, 2):
            amount *= i

    return amount

