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
# Assignment: 3.16 Lab: Still More Interpolation 
# Date: 6/9/2023 (Day/Month/Year)


# Formula: y = (slope)(x - x1) + y1

t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

#event 2
t = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))
print()
#figuring out V(x,y,z)
dt = t - t1 #change in time between events 1 and 2
VX = (x2 - x1) / dt  #Constant x velocity
VY = (y2 - y1) / dt  #Constant y velocity
VZ = (z2 - z1) / dt  #Constant z velocity

#position at t seconds

n = int(1)
nt = (t-t1)/4 #nt represents the interval between each event
t = t1


def interval ():
    dt = t - t1
    x = x1 + VX * dt
    y = y1 + VY * dt
    z = z1 + VZ * dt
    print( "At time " + format(t,'.2f') +" seconds the object is at ("+format(x,'.3f') +", "+ format(y,'.3f') +", "+ format(z,'.3f')+")")
    
    return

interval()
t += nt
interval()
t += nt
interval()
t += nt
interval()
t += nt
interval()
t += nt


