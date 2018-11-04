#
import sys

gameMap =  [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
player1 = 'x'
player2 = 'o'

def printGameMap():
    
    global gameMap
    print('   0     1    2')
    for col, row in enumerate(gameMap):
        print(col, row)
        print(' ', '-' * 15)

def makeMove(player, x, y):
    
    global gameMap
    if gameMap[x][y] == ' ' and x <= 2 and x >= 0 and y <= 2 and y >= 0:
        gameMap[x][y] =  player
    else: return False
    return True

def clearGameMap():

    global gameMap
    for row in range(len(gameMap)):
        for col in range(len(gameMap)):
            gameMap[row][col] = ' '

def checkHorizontal(r):
    
    global gameMap
    if ' ' in gameMap[r]: return 0
    if 'x' in gameMap[r] and 'o' not in gameMap[r]: return 1
    if 'o' in gameMap[r] and 'x' not in gameMap[r]: return 2

def checkVertical(c):
    
    global gameMap
    col = []
    for row in gameMap:
        col.append(row[c])
    if ' ' in col: return 0
    if 'x' in col and 'o' not in col: return 1
    if 'o' in col and 'x' not in col: return 2

def checkDiagonal():

    global gameMap
    if gameMap[1][1] == 'x':
        if gameMap[0][0] == 'x' and gameMap[2][2] == 'x':
            return 1
    elif gameMap[1][1] == 'o':
        if gameMap[0][0] == 'o' and gameMap[2][2] == 'o':
            return 2
    return 0

def playerAction(player):

    move = input()
    row = int(move[0])
    col = int(move[1])
    validMove = makeMove(player, row, col)
    printGameMap()
    h = checkHorizontal(row)
    v = checkVertical(col)
    d = checkDiagonal()
    gameOver = checkGameOver(h, v, d)
    return validMove, gameOver

def checkGameOver(h, v, d):
    
    global gameMap
    spacesLeft = 0

    if h == 1 or v == 1 or d == 1:
        print('Player One wins')
        return True
    if h == 2 or v == 2 or d == 2:
        print('Player Two wins')
        return True

    for row in gameMap:
        if ' ' in row:
            spacesLeft += 1
    if spacesLeft <= 1:
        print('Draw!')
        return True
    return False

def startGameOver():
    
    clearGameMap()
    print('Play again(yes/no)?')
    answer = input()
    if answer != 'yes':
        sys.exit()
    return answer
#main
answer = 'yes'
validMove = False
h, v, d = 0, 0, 0

while answer == 'yes':
    
    printGameMap()
    print()
    h, v, d = 0, 0, 0

    while(not validMove):
        print('Player 1 enter your move : ')
        validMove, gameOver = playerAction(player1)

    validMove = False
    if gameOver:
        answer = startGameOver()
        continue

    while(not validMove):
        print('Player 2 enter your move : ')
        validMove, gameOver = playerAction(player2)

    validMove = False
    if gameOver:
        answer = startGameOver()
        continue
#end game        
