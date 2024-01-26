# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Rivan Adhikari, JT Swiderski, Cody Wu, Patrick Simon
# Section:      520
# Assignment:   9.15.1 Lab Word Puzzles
# Date:         23 Septemeber, 2023


def print_puzzle(puzzle):
  ''' Print puzzle as a long division problem. '''
  puzzle = puzzle.split(',')
  for i in range(len(puzzle)):
    if i == 1:
      print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
    print(f'{puzzle[i]: >16}')
    if i > 1 and i % 2 == 0:
      print(f"{'-'*len(puzzle[i]): >16}")


#create function for finding the 10 letters
def get_valid_letters(puzzle):
  letters = []
  for char in puzzle:
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      if char not in letters:
        letters.append(char)
  letters = ''.join(letters)
  return letters


#print(get_valid_letters('RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA'))


#Guess = input("Enter your guess here: ")
#create function for checking the validity of a guess
def is_valid_guess(letters, guess):
  check = get_valid_letters(guess)
  valid = True
  for char in check:
    if char not in get_valid_letters(letters) or len(check) != 10:
      valid = False
  return (valid)


#print(is_valid_guess('RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA',Guess))


#create a function for checking the user's guess
def check_user_guess(dividend, quotient, divisor, remainder):
  return (dividend == quotient * divisor + remainder)


#create a function for assigning the letters a number value
def make_number(a, b):
  num = 0
  pof = 10**(len(a) - 1)
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:

        num += j * pof
    pof /= 10
  return int(num)


#print(make_number('RUE', 'TAKEOURSIM'))
#create a function that converts the puzzle string into numbers
def make_numbers(a, b):
  a = a.split("|")
  left = a[0].split(",")
  right = a[1].split(",")

  dividend = right[0]
  quotient = left[0]
  divisor = left[1][:-1]
  remainder = right[-1]
  tuple = (make_number(dividend, b), make_number(quotient, b),
           make_number(divisor, b), make_number(remainder, b))
  return tuple


#create a main function that takes input for a puzzle string, prints the
#puzzle, asks the user for a guess, and outputs an appropriate message.


def main():
  puzzle = input("Enter a word arithmetic puzzle: ")
  print()
  #puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
  print_puzzle(puzzle)
  letters = get_valid_letters(puzzle)
  print()
  guess = input("Enter your guess, for example ABCDEFGHIJ: ")
  valid = is_valid_guess(letters, guess)
  if valid == False:
    print(
        'Your guess should contain exactly 10 unique letters used in the puzzle.')
    exit()
  tuple = make_numbers(puzzle, guess)
  check = check_user_guess(tuple[0], tuple[1], tuple[2], tuple[3])
  if check:
    print('Good job!')
  else:
    print('Try again!')


# def main():
#   # The lines below demonstrate what the print_puzzle function outputs.
#   puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
#   print()
#   print_puzzle(puzzle)

if __name__ == '__main__':
  main()
