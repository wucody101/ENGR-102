# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   Lab 2.10: More Linear Interpolation
# Date:         27 August 2023

t1 = 12 #sec
t2 = 85 #sec

x12 = 8 #m
y12 = 6 #m
z12 = 7 #m

x85 = -5 #m
y85 = 30 #m
z85 = 9 #m

xslope = (x85 - x12) / (t2 - t1)
yslope = (y85 - y12) / (t2 - t1)
zslope = (z85 - z12) / (t2 - t1)

x1 = xslope * (30 - 12) + 8
y1 = yslope * (30 - 12) + 6
z1 = zslope * (30 - 12) + 7

print("At time 30.0 seconds:")
print("x1 =", x1, "m")
print("y1 =", y1, "m")
print("z1 =", z1, "m")
print("-----------------------")

x2 = xslope * (37.5 - 12) + 8
y2 = yslope * (37.5 - 12) + 6
z2 = zslope * (37.5 - 12) + 7

print("At time 37.5 seconds:")
print("x2 =", x2, "m")
print("y2 =", y2, "m")
print("z2 =", z2, "m")
print("-----------------------")

x3 = xslope * (45 - 12) + 8
y3 = yslope * (45 - 12) + 6
z3 = zslope * (45 - 12) + 7

print("At time 45.0 seconds:")
print("x3 =", x3, "m")
print("y3 =", y3, "m")
print("z3 =", z3, "m")
print("-----------------------")

x4 = xslope * (52.5 - 12) + 8
y4 = yslope * (52.5 - 12) + 6
z4 = zslope * (52.5 - 12) + 7

print("At time 52.5 seconds:")
print("x4 =", x4, "m")
print("y4 =", y4, "m")
print("z4 =", z4, "m")
print("-----------------------")

x5 = xslope * (60 - 12) + 8
y5 = yslope * (60 - 12) + 6
z5 = zslope * (60 - 12) + 7

print("At time 60.0 seconds:")
print("x5 =", x5, "m")
print("y5 =", y5, "m")
print("z5 =", z5, "m")
