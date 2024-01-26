# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 3.19: Tau Challenge
# Date:         5 September 2023

from math import *

prec_digit = int(input("Please enter the number of digits of precision for tau: ")) # digits of precision
print(f"The value of tau to {prec_digit} digits is: {tau:.{prec_digit}f}")
