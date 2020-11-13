import random

board = [" "] * 9     # initially empty board
winningPosition = [ [0,4,8] , [2,4,6] , [0,3,6], [1,4,7] , [0,1,2] , [3,4,5] , [6,7,8] , [2,5,8] ]   # all possible winning states


# display board as 3 * 3 grid
def boardDisplay():
    print("----------")
    print(board[0],end="")
    print(" | ",end="")
    print(board[1],end="")
    print(" | ",end="")
    print(board[2])
    print("----------")
    print(board[3],end="")
    print(" | ",end="")
    print(board[4],end="")
    print(" | ",end="")
    print(board[5])
    print("----------")
    print(board[6],end="")
    print(" | ",end="")
    print(board[7],end="")
    print(" | ",end="")
    print(board[8])
    print("----------")

# check if position is empty to insert
def checkIfAvailable(pos): 
    if(board[pos] == " "):
        return 1
    else:
        return 0

# check if the player has inserted in any of the above winning positions
def checkWin(player):
    for x in winningPosition:
        if board[x[0]]==board[x[1]] and board[x[1]]==board[x[2]] and board[x[0]]!=" ":
            print(player+" Won")
            return 0
    for i in board:
        if i==" ":
            return 1
    
    print("Draw Match")  # if board is full

# check if player has inserted in two position and corresponding winning position is empty
def algoWin(player):
    n=-1

    for x in winningPosition:
        if (board[x[0]]==player and board[x[1]]==player) and checkIfAvailable(x[2])==1:
            n = x[2]
            break
        elif (board[x[1]]==player and board[x[2]]==player) and checkIfAvailable(x[0])==1:
            n = x[0]
            break
        elif (board[x[0]]==player and board[x[2]]==player) and checkIfAvailable(x[1])==1:
            n = x[1]
            break

    return n

# check if opponent has inserted in two position and corresponding winning position is empty
def stopPlayer(player):
    n = -1

    for x in winningPosition:
        if (board[x[0]]==player and board[x[1]]==player) and checkIfAvailable(x[2])==1:
            n = x[2]
            break
        elif (board[x[1]]==player and board[x[2]]==player) and checkIfAvailable(x[0])==1:
            n = x[0]
            break
        elif (board[x[0]]==player and board[x[2]]==player) and checkIfAvailable(x[1])==1:
            n = x[1]
            break
    
    return n

# check if player has inserted in one position and other two corresponding winning position is empty
def algoTryWin(player):
    n = -1

    for x in winningPosition:
        if board[x[0]]==player and checkIfAvailable(x[2]==1) and checkIfAvailable(x[1]==1):
            if checkIfAvailable(x[2]==1):
                n = x[2]
                break
            elif checkIfAvailable(x[1]==1):
                n = x[1]
                break
        elif board[x[1]]==player and checkIfAvailable(x[0]==1) and checkIfAvailable(x[2]==1):
            if checkIfAvailable(x[0]==1):
                n = x[0]
                break
            elif checkIfAvailable(x[2]==1):
                n = x[2]
                break
        elif board[x[2]]==player and checkIfAvailable(x[0]==1) and checkIfAvailable(x[1]==1):
            if checkIfAvailable(x[0]==1):
                n = x[0]
                break
            elif checkIfAvailable(x[1]==1):
                n = x[1]
                break
    return n

# random position from 0 to 8 which is empty
def randomPos():
    while(1):
        n = random.randint(0,8)
        if checkIfAvailable(n)==1:
            return n

# agent playing is x and opponent is y
def algoPlay(x,y):

    # x to win
    n = algoWin(x)

    if n==-1:
        # block agent
        n = stopPlayer(y)
    
    if n==-1:
        # x try to win
        n = algoTryWin(x)

    if n==-1:
        # random position
        n = randomPos()

    print("Agent inserted at ",end="")
    print(n)
    board[n] = x

def play():

    # empty board
    boardDisplay()

    flag = 1

    while(flag):
        # Agent 1 starts ("X")
        print("\nAgent 1 Playing\n")
        algoPlay("X","O")
        boardDisplay()

        if checkWin("Agent 1") == 1:
            print("\nAgent 2 Playing\n")
            algoPlay("O","X")
            boardDisplay()
            if checkWin("Agent 2") == 0:
                flag = 0
        else:
            flag = 0

if __name__ == "__main__":
    play()