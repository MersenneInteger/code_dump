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

gameOver()
time.sleep(10)

