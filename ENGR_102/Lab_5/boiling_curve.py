# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 5.4: Boiling Curve
# Date:         15 September 2023

from math import *

#Assign X values
XA = 1.3
XB = 5
XC = 30
XD = 120
XE = 1200

#Assign Y values
YA = 1000
YB = 7000
YC = 1.5e6
YD = 2.5e4
YE = 1.5e6

#Ask for excess temp.
xEst = float(input("Enter the excess temperature: "))

#Filter inputs
if (xEst <= 0 or xEst > 1200):
    print("Surface heat flux is not available")
    exit()

#Calculate Slope
#calculate in order ab to cd
mAB = (log(YB/YA)) / (log(XB/XA))
mBC = (log(YC/YB)) / (log(XC/XB))
mCD = (log(YD/YC)) / (log(XD/XC))
mDE = (log(YE/YD)) / (log(XE/XD))

#Calculate surface heat flux using functions
def AtoB(xEst):
    yEst = YA * (xEst/XA)**mAB
    return yEst

def BtoC(xEst):
    yEst = YB * (xEst/XB)**mBC
    return yEst

def CtoD(xEst):
    yEst = YC * (xEst/XC)**mCD
    return yEst

def DtoE(xEst):
    yEst = YD * (xEst/XD)**mDE
    return yEst

#Create if statements and print
if (xEst >= 1.3 and xEst < 5):
    print(f"The surface heat flux is approximately {AtoB(xEst):.0f} W/m^2")

elif (xEst >= 5 and xEst < 30):
    print(f"The surface heat flux is approximately {BtoC(xEst):.0f} W/m^2")

elif (xEst >= 30 and xEst < 120):
    print(f"The surface heat flux is approximately {CtoD(xEst):.0f} W/m^2")

elif (xEst >= 120 and xEst < 1200):
    print(f"The surface heat flux is approximately {DtoE(xEst):.0f} W/m^2")
