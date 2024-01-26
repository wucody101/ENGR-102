# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 3.17: Using Input
# Date:         5 September 2023

from math import *

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg) : ")) #asks for the mass
accel = float(input("Please enter the acceleration (m/s^2) : ")) #asks for the acceleration
force = mass * accel #math calculation
print(f"Force is {force:.1f} N") #prints with proper units and decimals
print('\n') #skips a line

print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm) : ")) 
scat_ang = float(input("Please enter the angle (degrees) : ")) 
radscat_ang = radians(scat_ang) #turns degrees to radians
wavelength = 2 * distance * sin(radscat_ang) #nm
print(f"Wavelength is {wavelength:.4f} nm")
print('\n')

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days) : "))
half = 3.8 #days
N0 = float(input("Please enter the initial amount (g) : "))
Nleft = N0 * 2 ** (-time/3.8) #g
print(f"Radon-222 left is {Nleft:.2f} g")
print('\n')

print("This program calculates the pressure given moles, volume, and temperature")
amount = float(input("Please enter the number of moles : "))
vol = float(input("Please enter the volume (m^3) : "))
temp = float(input("Please enter the temperature (K) : "))
gascon = 8.314 #m^3 Pa/K mol
press = (amount * gascon * temp) / vol #Pa
kpress = press / 1000 #kPa
print(f"Pressure is {kpress:.0f} kPa")
print('\n')
