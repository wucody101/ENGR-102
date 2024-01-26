# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 2.9: Using Variables
# Date:         25 August 2023

from math import *

mass = 27 #kg
accel = 1.5 #m/s^2
force = mass * accel #N
print("Force is", force, "N")

distance = 0.025 #nm
scat_ang = 35 #degrees
radscat_ang = radians(35) #turns degrees to radians
wavelength = 2 * distance * sin(radscat_ang) #nm
print("Wavelength is", wavelength, "nm")

time = 5 #days
half = 3.8 #days
N0 = 27 #g
Nleft = 27 * 2 ** (-5/3.8) #g
print("Radon-222 left is", Nleft, "g")

amount = 5 #mol
vol = 0.27 #m^3
temp = 415 #K
gascon = 8.314 #m^3 Pa/K mol
press = (amount * gascon * temp) / vol #Pa
kpress = press / 1000 #kPa
print("Pressure is", kpress, "kPa")
