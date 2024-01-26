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
# Assignment: 8.10 Lab: ASCII Clock
# Date: 16/10/2023 (Day/Month/Year)

#INPUTS

################ Creating my characters to be used ###################
#JT's code starts here

Mil = [[''],
       [''],
       [''],
       [''],
       ['']]
AMPM = Mil
#list of lists for AM/PM
PM =[['PPP M   M'],
     ['P P MM MM'],
     ['PPP M M M'],
     ['P   M   M'],
     ['P   M   M']]

AM =[[' A  M   M'],
     ['A A MM MM'],
     ['AAA M M M'],
     ['A A M   M'],
     ['A A M   M']]

#List of lists to draw numbers
Numbers = {0:[['000 '],
              ['0 0 '],
              ['0 0 '],
              ['0 0 '],
              ['000 ']],

          1:[[' 1  '],
             ['11  '],
             [' 1  '],
             [' 1  '],
             ['111 ']],

          2:[['222 '],
             ['  2 '],
             ['222 '],
             ['2   '],
             ['222 ']],

          3:[['333 '],
             ['  3 '],
             ['333 '],
             ['  3 '],
             ['333 ']],

          4:[['4 4 '],
             ['4 4 '],
             ['444 '],
             ['  4 '],
             ['  4 ']],

          5:[['555 '],
             ['5   '],
             ['555 '],
             ['  5 '],
             ['555 ']],

          6:[['666 '],
             ['6   '],
             ['666 '],
             ['6 6 '],
             ['666 ']],

          7:[['777 '],
             ['  7 '],
             ['  7 '],
             ['  7 '],
             ['  7 ']],

          8:[['888 '],
             ['8 8 '],
             ['888 '],
             ['8 8 '],
             ['888 ']],

          9:[['999 '],
             ['9 9 '],
             ['999 '],
             ['  9 '],
             ['999 ']]}

Colon = [['  '],
         [': '],
         ['  '],
         [': '],
         ['  ']]
#end of JT code
################ Taking Inputs #################
#Rivan's code begins here
Time = input('Enter the time: ')
Type = input('Choose the clock type (12 or 24): ')
Char = input('Enter your preferred character: ')

#creating list of lists to format output
New_Numbers = {1:[[],[],[],[],[]],2:[[],[],[],[],[]],3:[[],[],[],[],[]],4:[[],[],[],[],[]],5:[[],[],[],[],[]],6:[[],[],[],[],[]],7:[[],[],[],[],[]],8:[[],[],[],[],[]],9:[[],[],[],[],[]],0:[[],[],[],[],[]]}
#Creating list of valid characters
Valid = 'abcdeghkmnopqrsuvwxyz@$&*='
Good = False

############### If we get a valid input, we change the Number templates to the appropriate Character
while not Good:
  if Char in [' ',''] :
    Good = True
    New_Numbers = Numbers
  elif Char in Valid:
    Good = True
    for i in range(len(Numbers)):
      for j in range(len(Numbers[i])):
        for k in range(len(Numbers[i][j][0])):
          if Numbers[i][j][0][k] in '0123456789':
            New_Numbers[i][j] += Char
          else:
            New_Numbers[i][j] += ' '
  else: 
    Char = input("Character not permitted! Try again: ")

print()
    
#End Rivan's code
################# Spliting the Time Var into Hours, Minutes #################
#Cody's code begins here
Time = Time.split(':')
Hour = int(Time[0])
Minute = int(Time[1])

################# Converting Time to 12 Hour Format #################
if Type == '12':
    if Hour == 0:
        Hour = 12
        AMPM = AM
    elif Hour > 12:
        AMPM = PM
        Hour = Hour - 12
    elif Hour == 12:
        AMPM = PM
    else:
        Hour = Hour
        AMPM = AM
    if Hour < 10:
        Hour =  Hour
    else:
        Hour = str(Hour)
    if Minute < 10:
        Minute = '0'+str(Minute)
Hour = str(Hour)
Minute = str(Minute)

################# Building outputs out of our New Number Templates Still as a list ###################

output1 = []
output2 = []
output3 = []
output4 = []
output5 = []

#changing characters in output to specified character
for dig in Hour:

  output1.append(New_Numbers[int(dig)][0])
  output2.append(New_Numbers[int(dig)][1])
  output3.append(New_Numbers[int(dig)][2])
  output4.append(New_Numbers[int(dig)][3])
  output5.append(New_Numbers[int(dig)][4])

output1.append(Colon[0])
output2.append(Colon[1])
output3.append(Colon[2])
output4.append(Colon[3])
output5.append(Colon[4])
#end of Cody's code
#changing characters in output to specified character
#Patrick's code begins here
for dig in Minute:

  output1.append(New_Numbers[int(dig)][0])
  output2.append(New_Numbers[int(dig)][1])
  output3.append(New_Numbers[int(dig)][2])
  output4.append(New_Numbers[int(dig)][3])
  output5.append(New_Numbers[int(dig)][4])

output1.append(AMPM[0])
output2.append(AMPM[1])
output3.append(AMPM[2])
output4.append(AMPM[3])
output5.append(AMPM[4])

################ Joining my outputs into single strings ########################

Str_Output = ['','','','','']
for i in output1:
  Str_Output[0] += ''.join(i)
for i in output2:
  Str_Output[1] += ''.join(i)

for i in output3:
  Str_Output[2] += ''.join(i)

for i in output4:
  Str_Output[3] += ''.join(i)

for i in output5:
  Str_Output[4] += ''.join(i)
separator = ' '

############## Removing the last space if we are in military time ##############

Mil_Print = ['','','','','']

if AMPM == Mil:
  for i in range(len(Str_Output)):
    for j in range(len(Str_Output[i])-1):
      Mil_Print[i] += str(Str_Output[i][j])

  Str_Output = Mil_Print

############### Printing my outputs on individual Lines #############

for i in Str_Output:
  print(i)

#end of patricks code
