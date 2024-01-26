# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 6.16: Balancing Numbers
# Date:         25 September 2023

n = int(input("Enter a value for n: "))         #inputs
sum1 = 0
sum2 = n + 1
r = 1

for i in range(1, n):                           #adds all numbers from 1 to n-1
    sum1 += i

while sum1 > sum2:                              #checks for balancing number or not
    r += 1
    sum2 += n + r

if sum1 == sum2:
    print(f"{n} is a balancing number with r={r}")
else:
    print(f"{n} is not a balancing number")
