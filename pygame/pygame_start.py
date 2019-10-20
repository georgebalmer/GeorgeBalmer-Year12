import pygame
# -- Global Constants


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

sun_x = 40

sun_y = 100
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
    sun_x = sun_x + 5
    # -- screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - the clock tics over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
           
           
