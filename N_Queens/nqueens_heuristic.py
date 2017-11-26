#Name: Ralph Pereira
#Desc: A huristic search that uses two different 2-D array's, one to store the queens and one to store the values.
#       The values are calculated after each move of the queen, the queens are initally placed randomly.
#       Each move is is done by the row, a loop itrates through the array and adds up all the conflicts, and moves to the
#       least conflicting piece
import random
import copy
#creates a board 
def CreateBoard(n):
    return [[0 for i in range(n)]for j in range (n)]
#prints out the board
def PrintBoard(board):
    for y in range (0, len(board)): 
        print(board[y])
#checks if the numbers passed are within the scope of the board
def checkInRange(i, j):
    return i >= 0 and j >= 0 and i < BoardSize and j < BoardSize
#logic behind checking the row col and diagonal, this is done very sloppy but it works!
def CalcAll(cost, board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 1:
                for k in range(1, len(board)):
                    if checkInRange(i + k, j):
                        cost[i+k][j] += 1
                        if board[i+k][j] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i - k, j):
                        cost[i - k][j] += 1
                        if board[i - k][j] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i, j + k):
                        cost[i][j + k] += 1
                        if board[i][j + k] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i, j - k):
                        cost[i][j - k] += 1
                        if board[i][j - k] == 1:
                            break
                    else:
                        break
                


                for k in range(1, len(board)):
                    if checkInRange(i + k, j+k):
                        cost[i+k][j+k] += 1
                        if board[i+k][j+k] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i - k, j-k):
                        cost[i - k][j-k] += 1
                        if board[i - k][j-k] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i-k, j + k):
                        cost[i-k][j + k] += 1
                        if board[i-k][j + k] == 1:
                            break
                    else:
                        break
                for k in range(1, len(board)):
                    if checkInRange(i+k, j - k):
                        cost[i+k][j - k] += 1
                        if board[i+k][j - k] == 1:
                            break
                    else:
                        break
#basic runner method, creates the board, populates it, prints it, runs hill climber to solve
#then prints the board again
def SolveQueens():
    board = CreateBoard(BoardSize)
    cost = CreateBoard(BoardSize)
    PopulateBoard(board,cost)
    CalcAll(cost, board)
    print("Before")
    PrintBoard(board)
    print(HillClimb(board, cost))
    print("SOLVING...\n After")
    PrintBoard(board)


#sudo-randomly place the queens on the board, it places the pieces on the spot with the least number of conflicts in order to make it easier 
# for the hill climb
def PopulateBoard(board, cost):
    random.seed(rs)
    for x in range (0, len(board)):
      cost = CreateBoard(BoardSize)
      CalcAll(cost, board)
      indices = [i for i, c in enumerate(cost[x]) if c == min(cost[x])]
      board[x][indices[random.randint(0,len(indices)-1)]] = 1
#Checks to see if the board is complete, if all the queens have an attack value of zero the board is done
def IsComplete(board, cost):
    for x in range(BoardSize):
        for y in range(BoardSize):
            if board[x][y] == 1 and cost[x][y] != 0:
                return False
    return True
#main logic behind the hill climber
def HillClimb(board, cost):
    #tracker to see if the board has run too many times
    mSum  = numboards= 0
    #while the board is not complete
    while not IsComplete(board, cost):
        #run through the rows of the board
        for x in range(BoardSize):
            #current index of the queen in the row
            queenIndex = board[x].index(1)
            #if there is more than one smallest digit it will store them in all in an array
            #this is done so that it doesn't just pick the first smallest all the time
            indices = [i for i, c in enumerate(cost[x]) if c == min(cost[x] )]
            #if the queen's spot is bigger than the smallest spot it will put the queen down on that spot
            if cost[x][queenIndex] > cost[x][indices[0]]:
                board[x][queenIndex] = 0
                minValue = indices[random.randint(0,len(indices)-1)]
                board[x][minValue] = 1
                queenIndex = x
                cost = CreateBoard(BoardSize)
                CalcAll(cost, board)
        #if the hill climb has tried to solve the board more than the boardsize cube it will move a random piece
        #this is to kick it out of a potental valley 
        if mSum >= (BoardSize**3):
            mSum = 0
            spot = random.randint(0, BoardSize-1)
            for i in range(BoardSize):
                if board[spot][i] == 1:
                    if checkInRange(spot, i+1):
                        board[spot][i] = 0
                        board[spot][i+1] = 1
                    else:
                        board[spot][i] = 0
                        board[spot][i-1] = 1
        mSum += 1
        numboards += 1
    return numboards


BoardSize = int(input('Please input the number of queens: '))
rs = int(input('Please input the seed: '))
SolveQueens()