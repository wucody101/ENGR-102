# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rivan Adhikari, Cody Wu, JT Swiderski, Patrick Simon
# Section: 520
# Assignment: 11.9
# Date: 6/11/2023

#creat list of valid inputs
file_name = input("Enter the name of the file: ")
valid = []
#open the file
passports = open(file_name, "r")
passport_content = passports.read()
#print(passport_content)
#split into each individual passport
passport = passport_content.split("\n\n")
original = passport_content.split("\n\n")
validnum = 0
#print(len(passport))
num = 0
listvalid = []
for i in passport:
  
  
  if '\n' in i:
    i = i.replace('\n', ' ')
  i = i.split(' ')
  # i = i.split('\n')
  #print(i)
  for piece in i:
    piece = piece.split(':')
  #print(repr(i))
  byr, iyr, eyr, hgt, hcl, cid, pid = 0, 0, 0, 0, 0, 0, 0
  for piece in i:
    #print(repr(piece[0:2]))
    if piece[0:3] == "byr":
      byr = 1
    if piece[0:3] == "iyr":
      iyr = 1
    if piece[0:3] == "eyr":
      eyr = 1
    if piece[0:3] == "hgt":
      hgt = 1
    if piece[0:3] == "hcl":
      hcl = 1
    if piece[0:3] == "cid":
      cid = 1
    if piece[0:3] == "pid":
      pid = 1
  if byr + iyr + eyr + hgt + hcl + cid + pid == 7:
    validnum += 1
    valid.append(i)
    listvalid.append(num)

  num += 1
validoutput = []
for i in listvalid:
  #print(original[i])
  validoutput.append(original[i])

  # if piece[0] == "byr":

# print(valid)
# print(validnum)
# print(listvalid)
#write new file to write in valid passports
#print(validoutput)

reviewed = open("valid_passports.txt", "w+")
num = 0
for i in validoutput:
  num += 1
  reviewed.write("".join(i))
  if num != len(validoutput):
    reviewed.write("\n\n")
#print(reviewed)

print(f'There are {validnum} valid passports')
#close the file
passports.close()
reviewed.close()
