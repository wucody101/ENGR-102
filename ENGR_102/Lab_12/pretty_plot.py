# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   12.14 : Lab: Pretty Plot
# Date:         18 November 2023

import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1.02, 0.095], [-0.095, 1.02]])
v = np.array([0, 1])
Vprime = M @ v
plt.scatter([0], [1])
plt.scatter([Vprime[0]], [Vprime[1]])
for i in range(250) :
    Vprime = M @ Vprime
    plt.scatter(Vprime[0], Vprime[1])

plt.xlabel('x') #label
plt.ylabel('y')
plt.suptitle('Spiral Graph')    #title
plt.show()
