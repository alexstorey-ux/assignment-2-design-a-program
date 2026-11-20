#shrump
#alex david storey
#monday 20th november 2026 -> thursday 25th febuary 2027

#importing pygame
import time
import pygame
from pygame.locals import *

#initialising pygame
pygame.init()

#set up game window
screen = pygame.display.set_mode((700, 500))

#caption game window
pygame.display.set_caption('Shrump')

clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
screen.fill(BLACK)
pygame.display.flip()
clock.tick(60)

# main game loop
while True:



# This MUST happen after all the other drawing commands.
pygame.display.flip()

#IDLE friendly quitting
for event in pygame.event.get():
  if event.type == QUIT:
    pygame.quit()
    sys.exit()
