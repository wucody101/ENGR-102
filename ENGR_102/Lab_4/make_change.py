# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Rivan Adhikari 
# Cody Wu
# John Swierski
# Patrick Simon 
# Section: 520
# Assignment: 4.13 Lab: Make Change
# Date: 8/9/2023 (Day/Month/Year)

#calculating the total change
pay = float(input("How much did you pay?"))
cost = float(input("How much did it cost?"))
change = pay - cost
print("You received $" + format(change,'.2f') + " in change. That is...")

#declaring my variables
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if change >= 0.25:
  quarters = int(change // 0.25)
  change = change - (quarters * 0.25)

if quarters > 1:
  print(format(quarters,'.0f') + " quarters")
elif quarters == 1:
  print(format(quarters,'.0f') + " quarter")

if change >= 0.10:
  dimes = int(change // 0.10)
  change = change - (dimes * 0.10)

if dimes > 1:
  print(format(dimes,'.0f') + " dimes")
elif dimes == 1:
  print(format(dimes,'.0f') + " dime")

if change >= 0.05:
  nickels = int(change // 0.05)
  change = change - (nickels * 0.05)

if nickels > 1:
  print(format(nickels,'.0f') + " nickels")
elif nickels == 1:
  print(format(nickels,'.0f') + " nickel")


pennies = round(change / 0.01)
change = change - (pennies * 0.01)

if pennies > 1:
  print(format(pennies,'.0f') + " pennies")
elif pennies == 1:
  print(format(pennies,'.0f') + " penny")
