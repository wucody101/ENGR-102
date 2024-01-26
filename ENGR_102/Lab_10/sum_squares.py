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
# Assignment: 10.13 Lab: Sum Squares
# Date: 30/10/2023

def list_nums(num):
    list = []
    possible = []
    term = 0
    n = 0
    while term < num:
        possible.append(n**2)
        n+=1
        term = n**2

    for i in possible:
        for j in possible:
            for k in possible:
                for l in possible:
                    if i + j + k + l == num:

                        list.append(i**(1/2))
                        list.append(j**(1/2))
                        list.append(k**(1/2))
                        list.append(l**(1/2))
                        list.sort()
                        return list
                    elif i + j + k + l > num:
                        break

def count_sets(num): #comment
    list = []
    all = []
    count = 0
    possible = []
    term = 0
    n = 0
    while term <= num:
        possible.append(n**2)
        n+=1
        term = n**2
    #print(possible)
    for i in range(len(possible)+1):

        for j in range(len(possible)-i+1):
            if possible[-i] > num:
                break
            elif possible[-i] + possible[-i-j] + possible[-i-j] + possible[-i-j] < num:
                break
            for k in range(len(possible)-j-i+1):
                if possible[-i] + possible[-i-j] > num:
                    break
                elif possible[-i] + possible[-i-j] + possible[-i-j-k] + possible[-i-j-k]< num:
                    break
                for l in range(len(possible)-k-j-i+1):
                    #print(possible[-i] , possible[-i-j] , possible[-i-j-k] , possible[-i-j-k-l])
                    if possible[-i] + possible[-i-j] + possible[-i-j-k] > num:
                        break
                    elif possible[-i] + possible[-i-j] + possible[-i-j-k] + possible[-i-j-k-l] < num:
                        break
                    if possible[-i] + possible[-i-j] + possible[-i-j-k] + possible[-i-j-k-l] == num:
                        list = []
                        count += 1
                        list.append(int(possible[-i]**(1/2)))
                        list.append(int(possible[-i-j]**(1/2)))
                        list.append(int(possible[-i-j-k]**(1/2)))
                        list.append(int(possible[-i-j-k-l]**(1/2)))
                        list.sort()
                        #print(list)

    return(count)

#print(count_sets(100))                   
#num = int(input('enter a number'))
#print(list_nums(num))
