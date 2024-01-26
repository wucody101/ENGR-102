# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Patrick Simon, Rivan Adhikari, Cody Wu, John Swiderski 
# Section: 520
# Assignment: Lab 2.8: Linear Interpolation 
# Date: 25 8 2023

from math import *

print ("Part 1:")
t1 = 10                                #in minutes 
t2 = 55

p1 = 2027                              #in kilometers 
p2 = 23027

velo = (p2 - p1) / (t2 - t1)           #constant velocity      

p0 = 2027 - t1 * velo                  #p0 is time = 0

t25 = 25                               #t25 is time at 25 minutes

p25 = p0 + velo * t25

print (("For t = 25 minutes, the position p = "), (p25), ("kilometers"))    #final output

print ("Part 2:")

radius = 6745                  #in kilometers
circum = 2 * pi * radius          #formula for circumference
tfinal = 300

ptotal = p0 + velo * tfinal    #position before bounded between 0-circum 
trip = ptotal % circum          #trip is the total distance divided by the circumference
print (("For t = 300 minutes, the position p = "), (trip), ("kilometers"))
