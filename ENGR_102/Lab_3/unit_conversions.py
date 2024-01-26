# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Rivan Adhikari 
# John Swiderski 
# Cody Wu
# Simon Patrick 
# Section: 520
# Assignment: Lab 3.15: Unit Conversions
# Date: 01 / 09 / 2023

def lbToN(val):                  #pounds to newtons 
  newton = val * 4.4482189159
  return newton

def mToFt(val):                  #meters to feet
  feet = val * 3.28084 
  return feet

def atToKilopa(val):             #atmosphere to kilopascals 
  kilopa = val * 101.325
  return kilopa

def wattToBtu(val):             #watts to BTU 
  btu = val * 3.412141633
  return btu

def LsToGm(val):                #liters per second to US gallons per minute
  gallons = val * 15.850323141489
  return gallons

def celtofar(val):              #celsius to farhenheit
  far = val * (9/5) + 32
  return far

val = float(input("Please enter the quantity to be converted: "))
print(f"{val:.2f} pounds force is equivalent to {lbToN(val):.2f} Newtons")
print(f"{val:.2f} meters is equivalent to {mToFt(val):.2f} feet")
print(f"{val:.2f} atmospheres is equivalent to {atToKilopa(val):.2f} kilopascals")
print(f"{val:.2f} watts is equivalent to {wattToBtu(val):.2f} BTU per hour")
print(f"{val:.2f} liters per second is equivalent to {LsToGm(val):.2f} US gallons per minute")
print(f"{val:.2f} degrees Celsius is equivalent to {celtofar(val):.2f} degrees Fahrenheit")
