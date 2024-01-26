# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 7.27: Split List
# Date:         5 October 2023

numbers = input("Enter numbers: ")          #gets user input
ints = numbers.split()
i = 0

for nums in ints:                           #converts to int list
    nums = int(nums)
    ints[i] = nums
    i = i + 1

j = 0
left = 0
sum = 0
midstatus = 0
for nums in ints:                           #gets total sum
    sum += nums

for nums in ints:                           #checks for even split
    left += nums
    if (left == sum - left) :
        j += 1
        midstatus = 1
        break
    j += 1

leftlist = []
rightlist = []
if (midstatus == 1) :                           #prints
    for k in range(j) :
        leftlist.append(ints[k])
    for m in range(len(ints) - j) :
        rightlist.append(ints[m + j])
    print(f"Left: {leftlist}")
    print(f"Right: {rightlist}")
    print(f"Both sum to {int(sum/2)}")
else :
    print("Cannot split evenly")
