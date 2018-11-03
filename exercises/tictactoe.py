#
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

def checkDiagnol():

    global gameMap
    if gameMap[1][1] == 'x':
        if gameMap[0][0] == 'x' and gameMap[2][2] == 'x':
            return 1
    elif gameMap[1][1] == 'o':
        if gameMap[0][0] == 'o' and gameMap[2][2] == 'o':
            return 2
    return 0

def checkGameOver(h, v, d):
    
    if h == 1 or v == 1 or d == 1:
        print('Player One wins')
        return True
    if h == 2 or v == 2 or d == 2:
        print('Player Two wins')
        return True
    return False

answer = 'yes'
validMove = False
h, v, d = 0, 0, 0

while answer == 'yes':
    
    printGameMap()
    print()
    h, v, d = 0, 0, 0

    while(not validMove):
        print('Player 1 enter your move : ')
        p1Move = input()
        p1Row = int(p1Move[0])
        p1Col = int(p1Move[1])
        validMove = makeMove(player1, p1Row, p1Col)
    
    validMove = False
    printGameMap()
    h = checkHorizontal(p1Row)
    v = checkVertical(p1Col)
    d = checkDiagnol()
    gameOver = checkGameOver(h, v, d)

    if gameOver:
        clearGameMap()
        print('Play again(yes/no)?')
        answer = input()
        continue

    while(not validMove):
        print('Player 2 enter your move : ')
        p2Move = input()
        p2Row = int(p2Move[0])
        p2Col = int(p2Move[1])
        validMove = makeMove(player2, p2Row, p2Col)
    
    validMove = False
    printGameMap()
    h = checkHorizontal(p2Row)
    v = checkVertical(p2Col)
    d = checkDiagnol()
    gameOver = checkGameOver(h, v, d)

    if gameOver:
        clearGameMap()
        print('Play again(yes/no)?')
        answer = input()
        continue
#end game        
