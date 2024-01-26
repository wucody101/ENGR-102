# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rivan Adhikari, Cody Wu, JT Swiderski, Patrick Simon
# Section: 520
# Assignment: 12.13 Lab: Matplotlib Example
# Date: 17/11/2023

#As a team, we have gone through all required sections of the
#tutorial, and each team member understands the material

import matplotlib.pyplot as plt
import numpy as np

#part A
x = np.linspace(-2, 2)
line1, line2 = plt.plot(x, (x**2 / 8), x, (x**2 / 24))  #lines
plt.setp(line1, color='r', linewidth=2.0, label='f=2')  #plot
plt.setp(line2, color='b', linewidth=6.0, label='f=6')
plt.xlabel('x') #label
plt.ylabel('y')
plt.suptitle('Parabola plots with varying focal length')    #title
plt.legend(loc='lower left')    #legend
plt.show()

#part B
t = np.arange(-4., 4., (8 / 25))

plt.plot(t, (2 * t**3 + 3 * t**2 - 11 * t - 6), 'gs')   #plot
plt.xlabel('x values')  #label
plt.ylabel('y values')
plt.suptitle('Plot of cubic polynomial')    #title
plt.show()

#Part C
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)

func1 = np.sin(x)   #plot
func2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Plot of cos(x) and sin(x)')  #title

#plot 1
ax1.plot(3, 1, 1)
ax1.plot(x, func2, color='b', label='cos(x)')
ax1.set_ylabel("y = cos(x)")
ax1.grid()
ax1.legend(loc='lower right')
ax2.grid()
#plot 2
ax2.plot(3, 1, 1)
ax2.plot(x, func1, color='r', label='sin(x)')
ax2.set_ylabel("y = sin(x)")
plt.xlabel("X")
ax2.legend(loc = 'upper right')
plt.show()
