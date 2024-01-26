# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   11.11 : Lab: Barcode Checker
# Date:         8 November 2023

#open files and read
filename = input("Enter the name of the file: ") 
barcodes = open(filename, "r")
barcode_content = barcodes.readline()
valid_barcodes = open("valid_barcodes.txt", "w")

#calculations
nums = []
strnums = []
valid = 0
one = 0
while barcode_content != '':
    nums.clear()
    for digit in barcode_content:
        if digit != '\n':
            nums.append(int(digit))

    first = nums[0] + nums[2] + nums[4] + nums[6] + nums[8] + nums[10]
    second = nums[1] + nums[3] + nums[5] + nums[7] + nums[9] + nums[11]
    second *= 3
    together = first + second
    last = together % 10
    last = 10 - last

#valid check and write
    if last == nums[12]:
        strnums.clear()
        valid += 1
        for numbers in nums:
            strnums.append(str(numbers))
        if one == 0:
            valid_barcodes.write("".join(strnums))
            one = 1
        else :
            valid_barcodes.write("\n")
            valid_barcodes.write("".join(strnums))

    barcode_content = barcodes.readline()

barcodes.close()
valid_barcodes.close()

print(f'There are {valid} valid barcodes')
