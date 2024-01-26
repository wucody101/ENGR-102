# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Patrick Simon, Rivan Adhikari, Cody Wu, John Swiderski 
# Section: 520
# Assignment: Go Moves
# Date: 6 10 2023

#printing instructions
print("Welcome to our version of Go Moves! ")
print()
rules = "This game is meant for 2 players. \nBlack will be O and White will be o. \nBlack will go first and enter the coordinates \nfor where they wish to place their piece. \nThe board is numbered both in terms of rows \nand columns starting with 0 and going to 8. \nRows count from top to bottom and collumns \ncount from left to right. \nTo enter your desired coordinates, \ntype the number corresponding to the \nrow you wish to place in (space) the number \ncorresponding to the column you wish to place \nyour piece in. \nPlayers will alternate turns and you cannot \npalce a piece on top of one that is already \nthere. \nThe game ends when all the spaces are taken \nor if the word 'stop' is entered"
print(rules)
wow = 0

board = [[".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]

for i in range(9):
  for j in range(9):
    print(board[i][j],end='')
  print()
win = 0
turn = 0
user_input = []
move = []

#Creating a win condition and starting the game
while win == 0:
  print()
  #setting up the turn system, evens are Black and odds are White
  turn = turn % 2
  del move[:]
  if turn == 0:
    #taking a user input to make a move
    user_input = input('Enter a move for black \nformat:row column \n:')
  elif turn == 1:
    user_input = input('Enter a move for white \nformat:row column \n:')
    #command to end the game
  if user_input in ['stop']:
    break
    #command to restate instructions if players are confused
  if user_input in ['rules', 'help']:
    print(rules)
    continue
  user_input = user_input.split()

  #detects random invalid inputs
  try:
    for num in user_input:
      num = int(num)
  except:
    
    
    
    if wow == 0:
      print('Your move format is incorrect, please review the rules')
      print()
      print(rules)
    elif wow < 3:
      print()
      print("try again")
    elif wow  >= 3:
      print()
      print('dude its supposed to look like this')
      print()
      print('1 1')
      print()
    wow += 1
    continue
  for num in user_input:
    num = int(num)
    move.append(num)
  
  if len(move) != 2 or (move[0] not in range(9)) or (move[1] not in range(9)):
    print('Your move format is incorrect, please review the rules')
    print()
    print(rules)
    continue
  
################

  if board[move[0]][move[1]] in ['O','o']:
    print("Invalid move, there is a piece in that square. Enter a new turn")
  else:
    #Black's turn
    if turn == 0:
      board[move[0]][move[1]] = 'O'
      turn += 1
      #White's turn
    elif turn == 1:
      board[move[0]][move[1]] = 'o'
      turn += 1

  for i in range(9):
    for j in range(9):
      print(board[i][j],end='')
    print()
  del move[:]

print('Game has been ended.  Here is the final position:')

for i in range(9):
  for j in range(9):
    print(board[i][j],end='')
  print()

print('Life is good')
