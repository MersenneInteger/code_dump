import pygame, sys, random, time

checkErr = pygame.init()
if checkErr[1] > 0:
    print('{} errors occured, exiting...'.format(checkErr[1]))
    sys.exit()
else:
    print('Pygame initialized')

#initalize display
gameDisplay = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake')
x = 0
y = 1

fpsController = pygame.time.Clock()
#colors
#Color take R,G,B param
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(178, 34, 34)

#
snakePos = [100, 50]
snakeBody = [[100,50],[90,50],[80,50]]
foodPos = [random.randrange(1, 72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeDirection = direction

#game over function
def gameOver():
    
    font = pygame.font.SysFont('monaco', 72)
    #(text, Anti-Aliasing, color
    gameOverDisplay = font.render('Game Over!', True, red)
    gameOverLanding = gameOverDisplay.get_rect()
    gameOverLanding.midtop = (360, 15)
    gameDisplay.blit(gameOverDisplay, gameOverLanding)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#main

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeDirection = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeDirection = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeDirection = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeDirection = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validate direction
    if changeDirection == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeDirection == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeDirection == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeDirection == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    #change direction
    if direction == 'RIGHT':
        snakePos[x] += 10
    if direction == 'LEFT':
        snakePos[x] -= 10
    if direction == 'UP':
        snakePos[y] -= 10
    if direction == 'DOWN':
        snakePos[y] += 10

    #snake body
    snakeBody.insert(x, list(snakePos))
    if snakePos[x] == foodPos[x] and snakePos[y] == foodPos[y]:
        foodSpawn = False
    else:
        snakeBody.pop()
    if not foodSpawn:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    gameDisplay.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(gameDisplay,green,pygame.Rect(pos[x],pos[y],10,10))
    pygame.draw.rect(gameDisplay,red,pygame.Rect(foodPos[x],foodPos[y],10,10)) 
    pygame.display.flip()
    fpsController.tick(25)




