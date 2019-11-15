import pygame
# -- Global Constants
ball_list=[]

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

class Ball():
    def __init__(x_val,y_val,color,speed,ball_x_size,ball_y_size):
       x_val=20
       y_val=30
       colour=WHITE
       speed=20
       ball_x_size=20
       ball_y_size=20


# -- initialise PyGame
pygame.init()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- title of new window/screen
pygame.display.set_caption("my window")
# -- exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


### -- Game Loop
while not done:
    # -- user input and controls
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
       #ENDIF
    #NEXT EVENT
    # -- Game logic goes after this comment

    counter = 0 
    for counter in range (0, 9):
        ball_list[counter] = Ball()

   
    
    # -- screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.circle(screen, YELLOW, (40,100),40,0)
    pygame.draw.circle(Ball())
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - the clock tics over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
           
           
