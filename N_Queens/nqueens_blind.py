#Author: Ralph Pereira
#Desc: This Nqueens problem uses backtracking in order to solve the Problem
#Creates an n x n board for the program to run
def CreateBoard(n):
    return [[0 for i in range(n)]for j in range (n)]
#prints out the board
def PrintBoard(board):
    for y in range (0, len(board)): 
        print(board[y])
#places the queen down on the board
def PlaceQueen(board, row, col, piece):
    board[row][col] = piece
#Contains the main logic to solve the board
def SolveBoard(board,col):
  #If the column count is as big as the board, the queens are done being placed and we can return true
    if col >= len(board):
      return True
    #run a loop for the rows
    for x in range(0, len(board)):
      #if we can place on this row, place on the row and go onto the next column
      if CheckSafe(board, x, col):
        PlaceQueen(board, x, col,1)
        PrintBoard(board)
        print ("----------")
        #if the board has been solved
        if SolveBoard(board, col+1) == True:
          return True
        #reset the piece if the column hasn't been solved yet
        PlaceQueen(board, x, col,0)
    return False
#checks the row and across, I made it seperate for debugging purposes, It could all be in one method if needed
def CheckSafe(board, row, col):
  return True if CheckRow(board, row) and CheckAcross(board, row, col) else False
#checks if the row is safe
def CheckRow(board, row):
    for i in range (0,len(board)):
        if board[row][i] == 1:
            return False
    return True
#checks if the diagonal is safe
def CheckAcross(board, row, col):
    #check left diagonal
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    #check right diagonal
    for i,j in zip(range(row,len(board),1), range(col,-1,-1)):
      if board[i][j] == 1:
        return False
    return True
def SolveQueens():
  board = CreateBoard(BoardSize)
  if SolveBoard(board, 0) == False:
    print ("The board could not be solved")
    return False
  PrintBoard(board)
  return True
#adjust the size of the board 
BoardSize = int(input('Please input the number of queens: '))
SolveQueens()