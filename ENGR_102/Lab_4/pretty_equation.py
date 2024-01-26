# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Rivan Adhikari, John Swiderski, Patrick Simon, Cody Wu 
# Section: 520
# Assignment: 4.14 LAB: Pretty Equation 
# Date: 8 September 2023

from math import *
# inputs
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

#first coeff
if (A != 0):   
  if(A == 1):
    coef1 = str("x^2")
  elif (A == -1):
    coef1 = str("- x^2")
  elif (A > 0):
    coef1 = str(A) + "x^2"
  elif (A < 0):
    coef1 = "- " + str(abs(A)) + "x^2"
else :
  coef1 = ""

#first symbol
if (A != 0 and B > 0):
  Bsym = " + "
elif (B < 0):
  Bsym = " - "
elif (A == 0 or B == 0):
  Bsym = ""

#second coeff
if (B != 0):
  if(B == 1): 
    coef2 = str("x")
  elif (B == -1):
    coef2 = str("x")
  elif (B > 0):
    coef2 = str(B) + "x"
  elif (B < 0):
    coef2 = str(abs(B)) + "x"
else :
  coef2 = ""

#second symbol
if ((A != 0 or B!= 0) and C > 0):
  Csym = " + "
elif ((A != 0 or B!= 0) and C < 0):
  Csym = " - "
elif (B == 0) and (A == 0) or (C == 0):
  Csym = ""

#third coeff
if (C != 0):
  if (C > 0):
    coef3 = str(C)
  elif (C < 0):
    coef3 = str(abs(C))
elif C == 0 :
  coef3 = ""

print("The quadratic equation is "+ coef1 + Bsym + coef2 + Csym + coef3 + " = " + "0")
