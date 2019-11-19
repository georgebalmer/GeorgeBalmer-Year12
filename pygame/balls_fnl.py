# Import libraries
import pygame
import math
import random

# Define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,20,147)

ball_list = []

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 1400
screen_height = 700    
screen = pygame.display.set_mode([screen_width, screen_height])


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define the class Ball
class Ball():
    # Constructor function to define initial state of a ball object
    def __init__(self, x, y, col, x_speed, y_speed, width, length):
        # --- Class Attributes ---
        # Ball position
        self.x = x
        self.y = y

        # Ball's vector
        self.change_x = x_speed
        self.change_y = y_speed

        # Ball Size
        self.size = random.randrange(1,10)

        # Ball colour
        self.color = col

        #screen parameters
        width = screen_width_rand
        height = screen_length_rand

    # -- Class Methods ---
    # Defines the ball's movement
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x >= screen_width - self.size:
            self.change_x *= -1
        elif self.x <= 0 + self.size:
            self.change_x *= -1
        elif self.y >= screen_height - self.size:
            self.change_y *= -1
        elif self.y <= 0 + self.size:
            self.change_y *= -1
            
        if self.x >= screen_width - self.size:
            xrand = random.randrange(0, screen_width - 10)
            yrand = random.randrange(0, screen_height - 10)
            x_speedrand = random.randrange(1, 10)
            y_speedrand = random.randrange(1, 10)
            screen_width_rand = random.randrange(0, 1400)
            screen_length_rand = random.randrange(1, 700)
            colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
            theBall = Ball(xrand, yrand, colour, x_speedrand, y_speedrand, screen_width_rand, screen_length_rand)
            ball_list.append(theBall)
        elif self.x <= 0 + self.size:
            xrand = random.randrange(0, screen_width - 10)
            yrand = random.randrange(0, screen_height - 10)
            x_speedrand = random.randrange(1, 10)
            y_speedrand = random.randrange(1, 10)
            screen_width_rand = random.randrange(0, 1400)
            screen_length_rand = random.randrange(1, 700)
            colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
            theBall = Ball(xrand, yrand, colour, x_speedrand, y_speedrand, screen_width_rand, screen_length_rand)
            ball_list.append(theBall)
            
        elif self.y >= screen_height - self.size:
            xrand = random.randrange(0, screen_width - 10)
            yrand = random.randrange(0, screen_height - 10)
            x_speedrand = random.randrange(1, 10)
            y_speedrand = random.randrange(1, 10)
            screen_width_rand = random.randrange(0, 1400)
            screen_length_rand = random.randrange(1, 700)
            colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
            theBall = Ball(xrand, yrand, colour, x_speedrand, y_speedrand, screen_width_rand, screen_length_rand)
            ball_list.append(theBall)
        elif self.y <= 0 + self.size:
            xrand = random.randrange(0, screen_width - 10)
            yrand = random.randrange(0, screen_height - 10)
            x_speedrand = random.randrange(1, 10)
            y_speedrand = random.randrange(1, 10)
            screen_width_rand = random.randrange(0, 1400)
            screen_length_rand = random.randrange(1, 700)
            colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
            theBall = Ball(xrand, yrand, colour, x_speedrand, y_speedrand, screen_width_rand, screen_length_rand)
            ball_list.append(theBall)

        #end if
    #end proc

    #end def

    # Draws the ball on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    #end def

# Set game loop to false so it runs
done = False

# Create an object using the ball class

for count in range(0, 1):
    xrand = random.randrange(0, screen_width - 10)
    yrand = random.randrange(0, screen_height - 10)
    x_speedrand = random.randrange(1, 10)
    y_speedrand = random.randrange(1, 10)
    screen_width_rand = random.randrange(0, 1400)
    screen_length_rand = random.randrange(1, 700)
    colour = (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240))
    theBall = Ball(xrand, yrand, colour, x_speedrand, y_speedrand, screen_width_rand, screen_length_rand)
    ball_list.append(theBall)
#next count
# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball on the screen and then move it on
    for theBall in ball_list:
        theBall.draw(screen)
        theBall.move()
    #next
    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
    
#End While
pygame.quit()
