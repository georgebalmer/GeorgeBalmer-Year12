import pygame
import math
import random
# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

RANDCOLOR = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))

snow_list = []

# -- initialise PyGame
pygame.init()


# -- Blank Screen
screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
# -- title of new window/screen
pygame.display.set_caption("my window")
# -- exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#define class player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, col, direction, width, length):
        super().__init__()

        self.image = pygame.Surface([width, length])
        self.image.fill(YELLOW)

        self.rect.x = x
        self.rect.y = y

        self.change_x = direction

    def update(self):
        if event.key == pygame.K_RIGHT:
          self.change_x = 1
        if event.key == pygame.K_LEFT:
          self.change_x = -1
    
        
        





# Define the class Ball
class Snow(pygame.sprite.Sprite):
    # Constructor function to define initial state of a ball object
    def __init__(self, x, y, col, x_speed, y_speed, width, length):

        # Call the parent class (Sprite) constructor
        super().__init__()

        
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, length])
        self.image.fill(WHITE)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        # --- Class Attributes ---
        # Ball position
        self.rect.x = x
        self.rect.y = y

        # Ball's vector
        self.change_x = x_speed
        self.change_y = y_speed

        # Ball Size
        #self.size = (10,10)

        # Ball colour
        #self.color = col


    
    def update(self):
        self.rect.y = self.rect.y +2

        
           
                    

            #enddef

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for count in range(0, 10):
    xrand = random.randrange(0, screen_width - 10)
    yrand = random.randrange(0, screen_height)
    x_speedrand = random.randrange(1, 10)
    y_speedrand = random.randrange(1, 10)
    screen_width_rand = random.randrange(0, 1400)
    screen_length_rand = random.randrange(1, 700)
    colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
    theSnow = Snow(xrand, yrand, colour, x_speedrand, y_speedrand, 10,10)
    snow_list.append(theSnow)
    all_sprites_list.add(theSnow)

#self, x, y, col, direction, width, length)
    #self.image = pygame.Surface([width, length])
        #self.image.fill(RED)

        #self.rect.x = x
        #self.rect.y = y

        #self.change_x = direction
x =500
y = 20
x_speed = 0
thePlayer = Player(x, y, YELLOW, x_speed, 20, 10)
all_sprites_list.add(thePlayer)









### -- Game Loop
while not done:
    # -- user input and controls
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
       #ENDIF
    #NEXT EVENT
    # -- Game logic goes after this comment

   
   



    # -- screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - the clock tics over
    clock.tick(144)
# End While - End of game loop
pygame.quit()
           
           

