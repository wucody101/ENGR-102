# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 6.15: Juggler Sequence
# Date:         25 September 2023

n = int(input("Enter a positive integer: "))                #input

print("The Juggler sequence starting at", n, "is:")         #prints

count = 0

while n != 1:                                               #while n does not equal 1
        print(n, end = ', ')
        if (n % 2 == 0):                                    #even
            n = int(n ** (1/2))
        elif (n % 2 == 1):                                  #odd
            n = int(n ** (3/2))
        count += 1

print(n)                                                    #print last number
print("It took", count, "iterations to reach 1")            #print last
