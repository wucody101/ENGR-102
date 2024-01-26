# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 4.18: How Many Gadgets
# Date:         11 September 2023


x = int(input("Please enter a positive value for day: "))       #gets number of days

if (x < 0):                                                    #negative input case
    print("You entered an invalid number!")
    exit()

if (x > 0 and x <= 10):                                         # 1 - 10 days
    totsum = 10 * x
elif (x > 10 and x <= 50):                                      # 11 - 50 days
    totsum = 100 + (0.5 * (11 + x) * (x - 10))
elif (x > 50 and x < 101):                                      # 51 - 101 days
    totsum = 100 + (0.5 * (11 + 50) * (50 - 10)) + (50 * (x - 50))
else :
    totsum = 100 + (0.5 * (11 + 50) * (50 - 10)) + (50 * (100 - 50))

print("The sum total number of gadgets produced on day", x, "is", int(totsum))       #print
