# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 7.29: Kaprekar's Constant Challenge
# Date:         5 October 2023

count = 0
hightolow = 0
lowtohigh = 0

for k in range(10000) :
    finalnum = k
    for i in range(8) :                                                 #loop max 8 times
        if (finalnum == 0 or finalnum == 6174) :                        #end early if number reached
            break                               
        dig1 = finalnum // 1000                                         #gets digits
        finalnum %= 1000
        dig2 = finalnum // 100
        finalnum %= 100
        dig3 = finalnum // 10
        dig4 = finalnum % 10

        diglist = [dig1, dig2, dig3, dig4]                              #sorts digits
        diglist.sort()
        powerof = 1000
        hightolow = 0
        lowtohigh = 0

        for i in range(4) :                                             #converting and subtracting
            hightolow += diglist[3-i] * powerof
            lowtohigh += diglist[i] * powerof
            powerof /= 10
        finalnum = hightolow - lowtohigh
        finalnum = int(finalnum)
        count += 1

print(f"Kaprekar's routine takes {count} total iterations for all four-digit numbers")
