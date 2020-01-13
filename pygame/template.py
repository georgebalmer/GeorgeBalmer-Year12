import pygame
# -- Global Constants
map =   [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]
 

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- initialise PyGame
pygame.init()



## -- Define the class tile which is a sprite
class tile(pygame.sprite.Sprite):
 # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref

    def update(self):
        self.rect.x = self.rect.x + self.speedy

    def player_set_speedy(self,valy):
        self.speedy = valy

    def player_set_speedx(self,valx):
        self.speedx = valx
    
    
        
        


# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
      if map[x][y] == 1:
         my_wall = tile(BLUE, 20, 20, x*20, y *20)
         wall_list.add(my_wall)
         all_sprites_list.add(my_wall)
my_player = Player(YELLOW, 5, 5, 20, 20)
all_sprites_list.add(my_player)



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

            if event.key == pygame.K_LEFT:
                my_player.player_set_speedx= -3
            elif event.key == pygame.K_RIGHT:
                my_player.player_set_speedx(3)
            elif event.key == pygame.K_UP:
                my_player.player_set_speedy(-3)
            elif event.key == pygame.K_DOWN:
                my_player.player_set_speedy(3)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                my_player.player_set_speedx(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                my_player.player_set_speedy(0)

        
       #ENDIF
    #NEXT EVENT
    # -- Game logic goes after this comment

    # -- screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - the clock tics over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
