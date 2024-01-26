# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 7.26: Leet Speak
# Date:         4 October 2023

replacements = {'a' : '4', 'e' : '3', 'o' : '0', 's' : '5', 't' : '7'}      #dictionary
phrase = input("Enter some text: ")                                         #inputs
newphrase = ''                                              

for letter in phrase:                                                       #for each letter in the phrase
    if letter.lower() in replacements:                                      #if its in the dictionary
        newphrase += replacements[letter.lower()]                           #add the replacement to the new string
    else :
        newphrase += letter                                                 #or just leave it


print(f'In leet speak, "{phrase}" is:')
print(newphrase)
