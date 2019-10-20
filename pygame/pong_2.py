import pygame
# -- Global Constants
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1

padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


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
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               #write logic that happens on key press here
               y_padd = y_padd - 5
               

           elif event.key == pygame.K_DOWN:
               #write logic that happens after key press here
               y_padd = y_padd + 5
           #endif
       #endif
    #NEXT EVENT
    # -- Game logic goes after this comment
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if x_val>=620:
        x_direction = x_direction * -1
    #endif
    if x_val<=0:
        x_direction = x_direction * -1
    #endif
    if y_val>=460:
        y_direction = y_direction * -1
    #endif
    if y_val<=0:
        y_direction = y_direction * -1
    #endif
    
    # -- screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,WHITE, (x_padd,y_padd,padd_length,padd_width))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - the clock tics over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
           
           
