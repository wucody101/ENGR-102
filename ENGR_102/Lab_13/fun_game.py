# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Cody Wu
# Patrick Simon
# Rivan Adhikari
# John Swiderski
# Section: 520
# Assignment: Pente game (Topic 13 Team Lab)
# Date: 12/04/2023
import numpy as np
import turtle as t
import pygame

pygame.init()

pygame.mixer.music.load("TAMU War.mp3")
pygame.mixer.music.play()
t.setup(400, 400)
t.goto(0, 0)
Game_Rules = " -Pente is a game for 2 players.\n -Players take turns placing stones (represented by filled or empty circles) on the intersections on the board. The board is 19 x 19 with the axes numbered from 0 to 18 in the first quadrant of the x,y plane.\n -Player 1 will be represented by an open circle and will take the first turn. Player 2 will be represented by a filled circle.\n -Players can only place stones on empty intersections and (0,0) would be the bottom left corner of the board. \n -The goal of the game is to get 5 stones in a linear line either directly adjacent or diagonally, or to capture 5 pairs of your opponent's stones. \n -Stone captures only occur when exactly 2 of your oppent's stones are surrounded on either side by your stones. For example, if player 1 is x and player to is o, then x o o x would result in a capture.\n -Players can place stones in empty spaces between their opponent's stones without losing their stones. For example, x o _ x allows player 2 to place a stone in the blank space resulting in x o o x.\n Captures cause the board to regenerate, look for a new window\n-"
print(Game_Rules)
BoardPositionsX = []
BoardPositionsY = []

Board = np.zeros((19, 19))
# print(Board)
for i in range(-180, 200, 20):
  # print(i)
  BoardPositionsX.append(i)
  BoardPositionsY.append(i)

# print(BoardPositionsX)
# print(BoardPositionsY)


def Draw(Board, x, y):
  """Reloads the board graphic"""
  t.hideturtle()
  t.speed(0)
  t.setup(430, 430)
  t.penup()
  t.pensize(10)
  t.goto(-200, -200)
  t.pendown()
  t.goto(200, -200)
  t.goto(200, 200)
  t.goto(-200, 200)
  t.goto(-200, -200)
  t.penup()
  t.pensize(1)

  for i in x:

    t.goto(i, 200)
    t.pendown()
    t.goto(i, -200)
    t.penup()

  for i in y:
    t.goto(200, i)
    t.pendown()
    t.goto(-200, i)
    t.penup()


def outputBoard(Board):
  """Outputs the board into a txt file"""
  BraggingRights = open("braggingrights.txt", "w")
  BraggingRights.write(Board)
  BraggingRights.close()


def stringBoard(Board):
  """Turns the board into a string"""
  String = ''
  for i in range(len(Board)):
    for j in range(len(Board[i])):
      String += str(Board[i][j])
      String += ','
    String += '\n'
  return String


def runBoard(Board, BoardPostitionsX, BoardPositionsY):
  """Places the pieces on the board"""
  for i in range(19):
    for j in range(19):
      if Board[i, j] == 1:
        t.penup()
        t.goto(BoardPositionsX[i], BoardPositionsY[j] - 10)
        t.pendown()
        t.circle(10)
      if Board[i, j] == 2:
        t.penup()
        t.goto(BoardPositionsX[i], BoardPositionsY[j])
        t.pendown()
        t.dot(20)


def capturePrint(Board, BoardPositionsX, BoardPositionsY):
  t.clear()
  Draw(Board, BoardPositionsX, BoardPositionsY)
  runBoard(Board, BoardPositionsX, BoardPositionsY)


#########################################################
##                  Win Conditions
def wincheck(Board, move, P1Score, P2Score, Turn):
  """Checks if a player has won"""
  # Checking for Score of 5
  Win = False
  Winner = ''
  if P1Score >= 5:
    Win = True
    Winner = 'Player 1 wins by capturing 10 pieces'
  if P2Score >= 5:
    Win = True
    Winner = 'Player 2 wins by capturing 10 pieces'

  ##################### Checking for 5 in a row
  # -Vertical
  Vert = 1
  for i in range(1, 5):
    # print(Board[move[0],move[1]+i])
    if move[1] + i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0], move[1] + i] in [1.0]:
        Vert += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0], move[1] + i] in [2.0]:
        Vert += 1
      else:
        break
  for i in range(1, 5):
    # print(Board[move[0],move[1]-i])
    if move[1] - i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0], move[1] - i] in [1.0]:
        Vert += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0], move[1] - i] in [2.0]:
        Vert += 1
      else:
        break

  #############################
  ###   -Horizontal
  Hor = 1
  for i in range(1, 5):
    if move[0] + i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] + i, move[1]] in [1.0]:
        Hor += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] + i, move[1]] in [2.0]:
        Hor += 1
      else:
        break
  for i in range(1, 5):
    if move[0] - i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] - i, move[1]] in [1.0]:
        Hor += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] - i, move[1]] in [2.0]:
        Hor += 1
      else:
        break

  #########################################
  ### Diagonal Positive

  DiagPos = 1
  for i in range(1, 5):
    if move[0] + i not in range(19) or move[1] + i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] + i, move[1] + i] in [1.0]:
        DiagPos += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] + i, move[1] + i] in [2.0]:
        DiagPos += 1
      else:
        break
  for i in range(1, 5):
    if move[0] - i not in range(19) or move[1] - i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] - i, move[1] - i] in [1.0]:
        DiagPos += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] - i, move[1] - i] in [2.0]:
        DiagPos += 1
      else:
        break

  #########################################
  ### Diagonal Negative

  DiagNeg = 1
  for i in range(1, 5):
    if move[0] + i not in range(19) or move[1] - i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] + i, move[1] - i] in [1.0]:
        DiagNeg += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] + i, move[1] - i] in [2.0]:
        DiagNeg += 1
      else:
        break
  for i in range(1, 5):
    if move[0] - i not in range(19) or move[1] + i not in range(19):
      break
    if Turn % 2 == 0:
      if Board[move[0] - i, move[1] + i] in [1.0]:
        DiagNeg += 1
      else:
        break
    if Turn % 2 == 1:
      if Board[move[0] - i, move[1] + i] in [2.0]:
        DiagNeg += 1
      else:
        break

  #######################################
  ####### if any direction of 5 in a row is acheived, a winner is declaired.

  if Vert >= 5 or Hor >= 5 or DiagPos >= 5 or DiagNeg >= 5:

    Win = True
    if Turn % 2 == 0:
      Winner = 'White wins with 5 in a row'
    if Turn % 2 == 1:
      Winner = 'Black wins with 5 in a row'
  return (Win, Winner)


def capturecheck(Board, move, P1Score, P2Score, Turn):
  """Checking for captures and changing board if capture takes place and adding to capture score"""
  capture = False
  # -Vertical
  # Upwards
  up = True
  for i in range(1, 4):
    if move[1] + i not in range(19):
      up = False

  if up:
    if Turn % 2 == 0:
      if Board[move[0],
               move[1] + 1] in [2.0] and Board[move[0], move[1] + 2] in [
                   2.0
               ] and Board[move[0], move[1] + 3] in [1.0]:
        P1Score += 1
        Board[move[0],
              move[1] + 1], Board[move[0],
                                  move[1] + 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0],
               move[1] + 1] in [1.0] and Board[move[0], move[1] + 2] in [
                   1.0
               ] and Board[move[0], move[1] + 3] in [2.0]:
        P2Score += 1
        Board[move[0],
              move[1] + 1], Board[move[0],
                                  move[1] + 2], capture = 0.0, 0.0, True

  # -Vertical
  # Downwards
  down = True
  for i in range(1, 4):
    if move[1] - i not in range(19):
      down = False

  if down:
    if Turn % 2 == 0:
      if Board[move[0],
               move[1] - 1] in [2.0] and Board[move[0], move[1] - 2] in [
                   2.0
               ] and Board[move[0], move[1] - 3] in [1.0]:
        P1Score += 1
        Board[move[0],
              move[1] - 1], Board[move[0],
                                  move[1] - 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0],
               move[1] - 1] in [1.0] and Board[move[0], move[1] - 2] in [
                   1.0
               ] and Board[move[0], move[1] - 3] in [2.0]:
        P2Score += 1
        Board[move[0],
              move[1] - 1], Board[move[0],
                                  move[1] - 2], capture = 0.0, 0.0, True

  # -Horizontal
  # Right
  right = True
  for i in range(1, 4):
    if move[0] + i not in range(19):
      right = False

  if right:
    if Turn % 2 == 0:
      if Board[move[0] + 1, move[1]] in [
          2.0
      ] and Board[move[0] + 2, move[1]] in [2.0] and Board[move[0] + 3,
                                                           move[1]] in [1.0]:
        P1Score += 1
        Board[move[0] + 1, move[1]], Board[move[0] + 2,
                                           move[1]], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] + 1, move[1]] in [
          1.0
      ] and Board[move[0] + 2, move[1]] in [1.0] and Board[move[0] + 3,
                                                           move[1]] in [2.0]:
        P2Score += 1
        Board[move[0] + 1, move[1]], Board[move[0] + 2,
                                           move[1]], capture = 0.0, 0.0, True

    # -Horizontal
    # Left
  left = True
  for i in range(1, 4):
    if move[0] - i not in range(19):
      left = False

  if left:
    if Turn % 2 == 0:
      if Board[move[0] - 1, move[1]] in [
          2.0
      ] and Board[move[0] - 2, move[1]] in [2.0] and Board[move[0] - 3,
                                                           move[1]] in [1.0]:
        P1Score += 1
        Board[move[0] - 1, move[1]], Board[move[0] - 2,
                                           move[1]], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] - 1, move[1]] in [
          1.0
      ] and Board[move[0] - 2, move[1]] in [1.0] and Board[move[0] - 3,
                                                           move[1]] in [2.0]:
        P2Score += 1
        Board[move[0] - 1, move[1]], Board[move[0] - 2,
                                           move[1]], capture = 0.0, 0.0, True

  if left and up:
    if Turn % 2 == 0:
      if Board[move[0] - 1,
               move[1] + 1] in [2.0] and Board[move[0] - 2, move[1] + 2] in [
                   2.0
               ] and Board[move[0] - 3, move[1] + 3] in [1.0]:
        P1Score += 1
        Board[move[0] - 1,
              move[1] + 1], Board[move[0] - 2,
                                  move[1] + 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] - 1,
               move[1] + 1] in [1.0] and Board[move[0] - 2, move[1] + 2] in [
                   1.0
               ] and Board[move[0] - 3, move[1] + 3] in [2.0]:
        P2Score += 1
        Board[move[0] - 1,
              move[1] + 1], Board[move[0] - 2,
                                  move[1] + 2], capture = 0.0, 0.0, True

  if right and up:
    if Turn % 2 == 0:
      if Board[move[0] + 1,
               move[1] + 1] in [2.0] and Board[move[0] + 2, move[1] + 2] in [
                   2.0
               ] and Board[move[0] + 3, move[1] + 3] in [1.0]:
        P1Score += 1
        Board[move[0] + 1,
              move[1] + 1], Board[move[0] + 2,
                                  move[1] + 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] + 1,
               move[1] + 1] in [1.0] and Board[move[0] + 2, move[1] + 2] in [
                   1.0
               ] and Board[move[0] + 3, move[1] + 3] in [2.0]:
        P2Score += 1
        Board[move[0] + 1,
              move[1] + 1], Board[move[0] + 2,
                                  move[1] + 2], capture = 0.0, 0.0, True

  if left and down:
    if Turn % 2 == 0:
      if Board[move[0] - 1,
               move[1] - 1] in [2.0] and Board[move[0] - 2, move[1] - 2] in [
                   2.0
               ] and Board[move[0] - 3, move[1] - 3] in [1.0]:
        P1Score += 1
        Board[move[0] - 1,
              move[1] - 1], Board[move[0] - 2,
                                  move[1] - 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] - 1,
               move[1] - 1] in [1.0] and Board[move[0] - 2, move[1] - 2] in [
                   1.0
               ] and Board[move[0] - 3, move[1] - 3] in [2.0]:
        P2Score += 1
        Board[move[0] - 1,
              move[1] - 1], Board[move[0] - 2,
                                  move[1] - 2], capture = 0.0, 0.0, True

  if right and down:
    if Turn % 2 == 0:
      if Board[move[0] + 1,
               move[1] - 1] in [2.0] and Board[move[0] + 2, move[1] - 2] in [
                   2.0
               ] and Board[move[0] + 3, move[1] - 3] in [1.0]:
        P1Score += 1
        Board[move[0] + 1,
              move[1] - 1], Board[move[0] + 2,
                                  move[1] - 2], capture = 0.0, 0.0, True

    if Turn % 2 == 1:
      if Board[move[0] + 1,
               move[1] - 1] in [1.0] and Board[move[0] + 2, move[1] - 2] in [
                   1.0
               ] and Board[move[0] + 3, move[1] - 3] in [2.0]:
        P2Score += 1
        Board[move[0] + 1,
              move[1] - 1], Board[move[0] + 2,
                                  move[1] - 2], capture = 0.0, 0.0, True

  left = True
  for i in range(1, 4):
    if move[0] - i not in range(19):
      left = False

  return (Board, P1Score, P2Score, capture
          )  #### The returns for capturecheck(Board,move,P1Score,P2Score,Turn)


Win = False

Draw(Board, BoardPositionsX, BoardPositionsY)
P1Score = 0
P2Score = 0
Turn = 0
while not Win:

  if Turn % 2 == 0:
    user_input = input('Please enter your move for white\nformat:\nx y\n')

  if Turn % 2 == 1:
    user_input = input('Please enter your move for BLACK\nformat:\nx y\n')

  if user_input in ['Help', 'help', 'Rules', 'rules']:
    print(Game_Rules)
    continue

    #################################
    ### Various Commands

  if user_input in ['Resign', 'resign']:
    if Turn % 2 == 0:
      Winner = 'Black Wins because White is a quitter'
      Win = True
      continue
    if Turn % 2 == 1:
      Winner = 'White Wins because Black is a quitter'
      Win = True
      continue

  if user_input in ['Score', 'score']:
    print(f'White has {P1Score}\nBlack has {P2Score}')
    continue
  move = []
  Broken = False
  try:
    user_input = user_input.split()
    if len(user_input) != 2:
      print(Game_Rules)
      continue
    for i in user_input:
      move.append(int(i))
      if int(i) not in range(19):
        print(Game_Rules)
        print('The size of the board is 19x19 starting from 0 to 18 on x and y axis')
        Broken = True
    if Broken:
      continue
  except:
    print(Game_Rules)
    continue

  ############################################
  ###########
  if Board[move[0], move[1]] in [1, 2]:
    print('There is already a piece in that location, please review the board and try again')
    continue
  if Turn % 2 == 0:
    Board[move[0], move[1]] = 1
  if Turn % 2 == 1:
    Board[move[0], move[1]] = 2

  ######################################################

  CaptureCHECK = capturecheck(Board, move, P1Score, P2Score, Turn)
  Board = CaptureCHECK[0]

  P1Score = CaptureCHECK[1]
  P2Score = CaptureCHECK[2]
  if CaptureCHECK[3]:  #If capturecheck executed to True then we run the print function
    print("running capture print")
    print(Board)
    t.clear()  # i wasnt able to figure out how to just erase a circle without clearing the whole board
    Draw(Board, BoardPositionsX, BoardPositionsY)  #here, we redraw the board
  runBoard(Board, BoardPositionsX, BoardPositionsY)  #executes numpy board to the turtle output and draws our pieces
  Win, Winner = wincheck(Board, move, P1Score, P2Score,Turn)[0], wincheck(Board, move, P1Score, P2Score,Turn)[1]
  Turn += 1
  pass
print(Winner)
hold = True

while hold:
  input(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{Winner}\n\nDisplayed is the final board.\nDo you have any last words?\nSPEAK NOW OR FOREVER HOLD YOUR PEACE\n\n-')

  hold = False
  continue

outputBoard(stringBoard(Board))
