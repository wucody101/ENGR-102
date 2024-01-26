#input for digits

number = int(input("Enter a 4-digit integer:"))

 

#input power

power = int(input("Enter the power:"))

 

#split into digits


d1 = number // 1000

d234 = number % 1000

d2 = d234 // 100

d34 = d234 % 100

d3 = d34 // 10

d4 = d34 % 10  

#comparison

if (d1 ** power + d2 ** power + d3 ** power + d4 ** power == number):

    print(number, "with given power", power, "is a PDI")
else:
    print("0")

#print statement
