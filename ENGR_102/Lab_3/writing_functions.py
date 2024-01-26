# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 3.18: Writing Functions
# Date:         5 September 2023

from math import * 

def triangle(val):          #area of triangle
    tri_area = (sqrt(3) / 4) * (val**2)
    return tri_area

def square(val):            #area of square
    squ_area = val**2
    return squ_area

def pentagon(val):          #area of pentagon
    pent_area = ((val**2) * (sqrt(5*(5+2*sqrt(5))))) / 4
    return pent_area

def dodecagon(val):         #area of dodecagon
    dod_area = 3 * (val**2) * (2 + sqrt(3))
    return dod_area

num = float(input("Please enter the side length: "))
print(f"A triangle with side {num:.2f} has area {triangle(num):.3f}")
print(f"A square with side {num:.2f} has area {square(num):.3f}")
print(f"A pentagon with side {num:.2f} has area {pentagon(num):.3f}")
print(f"A dodecagon with side {num:.2f} has area {dodecagon(num):.3f}")
