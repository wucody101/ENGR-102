# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 9.6: Small functions
# Date:         25 October 2023

from math import *

def parta(r, a):
    svol = (4/3) * pi * pow(r, 3)                #sphere volume
    centertobase = sqrt(pow(r, 2) - pow(a, 2))
    h = r - centertobase
    ecvol = ((pi * pow(h, 2)) / 3) * (3 * r - h)     #endcap volume
    cyvol = pi * pow(a, 2) * 2 * (r - h)                   #cylinder volume
    fvol = svol - 2 * ecvol - cyvol             #final volume
    return fvol

def partb(n) :
    nums = []
    status = 0
    for i in range(1, n, 2):        #consider odd numbers only
        if i + i + 2 == n:
            nums.append(i)
            nums.append(i + 2)
            status = 1
        elif i + i + 2 + i + 4 == n:
            nums.append(i)
            nums.append(i + 2)
            nums.append(i + 4)
            status = 1
    if status == 1:
        return nums
    else:
        return False

def partc(char, name, company, email) :
    Ln = len(name)
    Lc = len(company)
    Le = len(email)
    max = Ln
    longest = name
    final = ""
    if (Lc > max) :                 #find biggest string
        max = Lc
        longest = company
    if (Le > max) :
        max = Le
        longest = email
    
    if longest == company:          #if company longest
        nsidelength = int((Lc + 4 - Ln) / 2)
        esidelength = int((Lc + 4 - Le) / 2)
        line1 = char * (max + 6)
        line2 = char + " " * nsidelength + name + " " * nsidelength + " " + char
        line3 = char + "  " + company + "  " + char
        line4 = char + " " * esidelength + email + " " * esidelength + char
        line5 = char * (max + 6)
        final = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5

    if longest == name:              #if name longest
        csidelength = int((Ln + 4 - Lc) / 2)
        esidelength = int((Ln + 4 - Le) / 2)
        line1 = char * (max + 6)
        line2 = char + "  " + name + "  " + char
        line3 = char + " " * csidelength + company + " " * csidelength + char
        line4 = char + " " * esidelength + email + " " * esidelength + char
        line5 = char * (max + 6)
        final = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
    
    if longest == email:             #if email longest
        nsidelength = int((Le + 4 - Ln) / 2)
        csidelength = int((Le + 4 - Lc) / 2)
        line1 = char * (max + 6)
        line2 = char + " " * nsidelength + name + " " * nsidelength + char
        line3 = char + " " * csidelength + company + " " * csidelength + char
        line4 = char + "  " + email + "  " + char
        line5 = char * (max + 6)
        final = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
    
    return final

def partd(numbers) :
    numbers.sort()
    minimum = min(numbers)      #add minimum
    median = len(numbers) / 2       
    if median % 1 == 0 :            #if even number
        median = (numbers[int(median)] + numbers[int(median - 1)]) / 2
    else :                          #if odd number
        median = (numbers[int(floor(median))])   #add maximum
    maximum = max(numbers)
    stats = (minimum, median, maximum)
    return stats

def parte(times, distances) :
    velocity = []
    for i in range(len(times) - 1):
        vel = (distances[i + 1] - distances[i]) / (times[i + 1] - times[i])     #calculation
        velocity.append(vel)            #adds to list
    
    return velocity

def partf(numbers) :
    for i in numbers:       #checks first number with all then second with all etc.
        for j in numbers:
            if i + j == 2027 :
                prod = i * j
                return prod
    
    return False
