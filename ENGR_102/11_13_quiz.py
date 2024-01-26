import numpy as np

numbers = np.zeros((100, 100))

data = open("/Users/codywu/FALL 2023/ENGR_102/module12quizF23.txt", "r")
integer_data = data.read()
integers = integer_data.split('\n')

incrementer = 0
for i in range(100) :
    for j in range(100) :
        numbers[i][j] = integers[incrementer]
        incrementer += 1

key1 = numbers[0][85] + numbers[1][85] + numbers[2][85] + numbers[3][85] + numbers[4][85] 

average = 0
for k in range(100) :
    average += numbers[4][k]
average /= 100
key2 = average

key3 = numbers[62][95] + numbers[62][96] + numbers[62][97] + numbers[62][98] + numbers[62][99]

minimum = numbers[0][0]
for l in range(100) :
    if numbers[0][l] < minimum:
        minimum = numbers[0][l]
key4 = minimum

maximum = numbers[29][0]
for p in range(100):
    if numbers[29][p] > maximum:
        maximum = numbers[29][p]
key5 = maximum

#print(key1, key2, key3, key4, key5)

numtoalpha = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p',
            16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

alphatonum = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15,
            'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

key = numtoalpha[key1] + numtoalpha[key2] + numtoalpha[key3] + numtoalpha[key4] + numtoalpha[key5]
print(key)

keyindex = 0
message = "zsyucavqojhpwomv"
deciphered = ""
for length in range(len(message)) :
    if keyindex == 5:
        keyindex = 0
    
    index = alphatonum[message[length]]
    index -= alphatonum[key[keyindex]]
    if index > 25:
        index -= 26
    if index < 0:
        index += 26
    
    print(index)
    deciphered += (numtoalpha[index])
    keyindex += 1

print(deciphered)
