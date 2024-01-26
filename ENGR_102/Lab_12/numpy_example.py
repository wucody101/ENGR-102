# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rivan Adhikari, Cody Wu, JT Swiderski, Patrick Simon
# Section: 520
# Assignment: 12.12 Lab: Numpy Example
# Date: 17/11/2023

#As a team, we have gone through all required sections of the
#tutorial, and each team member understands the material

import numpy as np

#Calculations
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
D = A @ B @ C
F = np.transpose(D)
E = np.sqrt(D)
E /= 2

#prints
print("A = ", A)
print()
print("B = ", B)
print()
print("C = ", C)
print()
print("D = ", D)
print()
print("D^T = ", F)
print()
print("E = ", E)
