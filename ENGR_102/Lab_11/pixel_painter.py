# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   11.12 : Lab: Pixel Painter
# Date:         8 November 2023

#open files and read
filename = input("Enter the filename: ") 
pixels = open(filename, "r")
pixel_content = pixels.readline()
characters = input("Enter a character: ")
txt = filename[0:-3]
pixel_triangle = open(f"{txt}txt", "w")

#variables
first = 0
while pixel_content != "":
    nums = []
    index = 0
    nums = pixel_content.strip().split(",")
    for a in range(len(nums)):
        nums[a] = int(nums[a])
    #print(nums)
    if first == 0:
        for i in nums :
            if index % 2 == 0:          #even
                for j in range(i):
                    pixel_triangle.write(" ")
                    #print(" ", end = "")

            else:         #odd
                for j in range(i):
                    pixel_triangle.write(characters)
                    #print(characters, end = "")
            
            index += 1
        first = 1
    
    else :
        pixel_triangle.write("\n")
        #print()
        for i in nums :
            if index % 2 == 0:          #even
                for j in range(i):
                    pixel_triangle.write(" ")
                    #print(" ", end = "")

            else:         #odd
                for j in range(i):
                    pixel_triangle.write(characters)
                    #print(characters, end = "")
            index += 1

    pixel_content = pixels.readline()

pixels.close()
pixel_triangle.close()

print(f"{txt}txt created!")
