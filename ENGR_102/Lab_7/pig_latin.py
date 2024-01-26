# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 7.25: Pig Latin
# Date:         4 October 2023

words = input("Enter word(s) to convert to Pig Latin: ")
splitlist = words.split()
final = ""
new = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']                 #checks vowels

for word in splitlist: 
    low = word.lower()
    if (low[0] in vowels) :                             #starts with vowel
        low = low + "yay "
        final += low
    else :
        vpos = -1
        for i in range(len(low)) :                      #starts with consonant
            if (low[i] in vowels) :
                vpos = i
                break
        if (vpos == -1) :                               #case if there is no vowel
            final += low
        else :
            new = low[vpos:]
            new += low[0:vpos]
            new += "ay "
            final += new

print(f'In Pig Latin, "{words}" is: {final}', end = "")
