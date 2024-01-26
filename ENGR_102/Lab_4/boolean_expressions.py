# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Rivan Adhikari
# Cody Wu
# John Swierski
# Patrick Simon
# Section: 520
# Assignment: 4.15 Lab: Boolean Expressions
# Date: 11/9/2023 (Day/Month/Year)

############ Part A ############
a = input("Enter True or False for a: ")      #input for a
if a == "t":
  a = True
elif a == "True":
  a = True
elif a == "T":
  a = True
elif a == "f":
  a = False
elif a == "False":
  a = False
elif a == "F":
  a = False
else:
  print ("Not an accepted input, please try again.")

b = input("Enter True or False for b: ")      #input for b
if b == "t":
  b = True
elif b == "True":
  b = True
elif b == "T":
  b = True
elif b == "f":
  b = False
elif b == "False":
  b = False
elif b == "F":
  b = False
else:
  print("Not an accepted input, please try again.")

c = input("Enter True or False for c: ")      #input for c
if c == "t":
  c = True
elif c == "True":
  c = True
elif c == "T":
  c = True
elif c == "f":
  c = False
elif c == "False":
  c = False
elif c == "F":
  c = False
else:
  print("Not an accepted input, please try again.")
 
############ Part B ############
d = a and b and c              #expression 1
e = a or b or c                #expression 2

print("a and b and c:", d)              
print("a or b or c:", e)

############ Part C ############
XOR = (a and (not b)) or ((not a) and b) 
print("XOR:", XOR)

odd = (not(a) and ((b and (not c)) or ((not b) and c))) or (a and ((not(b) and not(c)) or (b and c)))
print("Odd number:", odd)

############ Part D ############
comp1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
comp2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b))))
simp1 = (not(a) and not(b)) or (not(a) and b and not(c)) or (a and not(b))
simp2 = (a and not(b) and c) or (a and b and not(c)) or (a and not(b))
print("Complex 1:", comp1)
print("Complex 2:", comp2)
print("Simple 1:", simp1)
print("Simple 2:", simp2)
