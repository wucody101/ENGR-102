# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Patrick Simon, Rivan Adhikari, Cody Wu, John Swiderski 
# Section: 520
# Assignment: 6.11
# Date: 24 9 2023

side = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

#size of triangles
triangle = ((3 ** (1/2)) * (side ** 2)) / 4

#this is the base
area = triangle * (layers ** 2)

#building up the sides
i = 0
for i in range(layers+1):
    area += 3 * (side**2) * i

print('You need '+ format(area, '.2f') + ' m^2 of gold foil to cover the pyramid')