import pygame
# -- Global Constants

ball_width = 20
x_val = 150
y_val = 200
x_direction = 3
y_direction = 3

padd_width = 15
padd_length = 60
x_padd = 0
y_padd = 20
padd_direction=0

score = 0

x_padd2=625
y_padd2=20
padd_direction2=0

x_pos=0
y_pos=0
line_height=10

score_p2=0
score_p1=0

rally=0


fontName=pygame.font.match_font('arial')

padd_up=-8
padd_down=8

# -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

ball_colour=WHITE

## -- initialise PyGame

pygame.init()

# -- functions

def drawText (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)


 





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
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and y_padd >= 0:
                padd_direction = padd_up
            elif event.key == pygame.K_a and y_padd <= 580:
                padd_direction = padd_down
            elif event.key == pygame.K_UP and y_padd2 >=0:
                padd_direction2 = padd_up
            elif event.key == pygame.K_DOWN and y_padd2 <= 580:
                padd_direction2 = padd_down
            #End if
       elif event.type == pygame.KEYUP:
            padd_direction = 0
            padd_direction2 = 0
       
       #endif
    
    
    #NEXT EVENT
    # -- Game logic goes after this comment

    x_val = x_val + x_direction
    y_val = y_val + y_direction


    if x_val <= 15 and y_val >= y_padd-20 and y_val <= y_padd+60:
       x_direction = x_direction * -1
       ball_colour=BLUE
       rally=rally+1
       if x_direction>0 and y_direction>0:
             x_direction=x_direction+1
             y_direction=y_direction+1
       elif x_direction<0 and y_direction<0:
             x_direction=x_direction-1
             y_direction=y_direction-1
       #endif
       
    #endif

    if x_val >= 610 and y_val >= y_padd2-20 and y_val <= y_padd2+60:
       x_direction = x_direction * -1
       ball_colour=YELLOW
       rally=rally+1
       if x_direction>0 and y_direction>0:
             x_direction=x_direction+1
             y_direction=y_direction+1
       elif x_direction<0 and y_direction<0:
             x_direction=x_direction-1
             y_direction=y_direction-1
       #endif
    #endif


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

    

    y_padd += padd_direction
    y_padd2 += padd_direction2
    

    if x_val <= 0:
        score_p2 = score_p2+1
        rally = 0
        x_direction=3
        y_direction=3
    #endif



    if x_val >= 620:
        score_p1 =score_p1+1
        rally = 0
        x_direction=3
        y_direction=3
    #endif


    


    # -- screen background is BLACK

    screen.fill (BLACK)

    # -- Draw here

    pygame.draw.rect(screen,ball_colour, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,BLUE, (x_padd,y_padd,padd_width,padd_length))
    pygame.draw.rect(screen,YELLOW, (x_padd2,y_padd2,padd_width,padd_length))
    
    drawText(screen, str(score_p1),25, 25, 3)
    drawText(screen, str(score_p2),25, 615, 3)
    drawText(screen, str("rally =  "),25, 290, 3)
    drawText(screen, str(rally),25, 330, 3)
    
    # -- flip display to reveal new position of objects

    pygame.display.flip()

    # - the clock tics over

    clock.tick(60)

# End While - End of game loop

pygame.quit()
           
