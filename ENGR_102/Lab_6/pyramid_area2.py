# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Patrick Simon, Rivan Adhikari, Cody Wu, John Swiderski 
# Section: 520
# Assignment: 6.12
# Date: 24 9 2023

side = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

#size of triangles
triangle = ((3 ** (1/2)) * (side ** 2)) / 4

#this is the base
area = triangle * (layers ** 2)

#building up the walls
square = side ** 2
num = 3 * (sum(range(layers+1))) #counts the number of squares on the walls
area += (num * square)

print('You need '+ format(area, '.2f') + ' m^2 of gold foil to cover the pyramid')