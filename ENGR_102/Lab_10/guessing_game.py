# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   10.15 : Lab: Guessing Game
# Date:         2 November 2023

def check_number(guess):        #checks if too high or too low or equal
    if guess > secret:
        return 1
    elif guess < secret: 
        return 0
    elif guess == secret:
        return -1

def read_result(result, count):         #prints
    if result == 1:
        print("Too high!")
    if result == 0:
        print("Too low!")
    if result == -1:
        print(f'You guessed it! It took you {count} guesses.')


secret = 27
status = False
count = 0
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
while not status :           #loops until right answer
    valid = False
    while not valid:
        try:
            guess = input("What is your guess? ")
            if '.' in guess:
                while not valid:
                    guess = input("Bad input! Try again: ")
                    if '.' not in guess:
                        guess = int(guess)
                        valid = True
            else :
                guess = int(guess)
                valid = True
        except ValueError:
            while not valid:
                guess = input("Bad input! Try again: ")
                if not guess.isalpha() and '.' not in guess:
                    guess = int(guess)
                    valid = True
    count += 1
    result = check_number(guess)
    read_result(result, count)
    if result == -1:
        status = True
