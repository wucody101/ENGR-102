# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 6.13: Howdy Whoop
# Date:         25 September 2023

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

for i in range(1, 101):                                     #from 1 - 100
    if (i % int1 == 0 and i % int2 == 0):             #divisible by both
        print("Howdy Whoop")
    elif (i % int1 == 0):                               #divisible by int1
        print("Howdy")
    elif (i % int2 == 0):                               #divisible by int2
        print("Whoop")
    else:
        print(i)
