# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 4.19: Calculate Roots
# Date:         11 September 2023

from math import *
#asks for coefficients
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if (a == 0 and b != 0 and c != 0):                                          #a = 0
    x = -c / b
    print("The root is x =", x)

elif (a == 0 and b == 0 and c !=0):                                               #a = b = 0 but c != 0
    print("You entered an invalid combination of coefficients!")

elif ((b**2 - (4 * a * c)) > 0):                                                 #normal case
    root1 = (-b + sqrt(b**2 - (4 * a * c))) / (2 * a)
    root2 = (-b - sqrt(b**2 - (4 * a * c))) / (2 * a)
    if (root1 > root2):
        print("The roots are x =", root1, "and x =", root2)
    elif (root2 > root1):
        print("The roots are x =", root2, "and x =", root1)
    elif (root1 == root2):
        print("The root is x =", root1)

elif ((b**2 - (4 * a * c)) == 0):                                                 #0 case
    root0 = -b / (2 * a)
    print("The root is x =", root0)

elif ((b**2 - (4 * a * c)) < 0):                                                  #imaginary case
    imag1 = -b/(2 * a)
    imag2 = sqrt(abs(b**2 - (4 * a * c))) / (2 * a)
    if (imag1 + imag2 > imag1 - imag2):
        print("The roots are x =", imag1, "+", str(imag2) + "i", "and x =", imag1, "-", str(imag2) + "i")
    if (imag1 - imag2 > imag1 + imag2):
        print("The roots are x =", imag1, "-", str(imag2) + "i", "and x =", imag1, "+", str(imag2) + "i")
