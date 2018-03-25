import pygame
import sys
import time
import pygbutton
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

window_size_x = 500
window_size_y = 500

window_size = (window_size_x, window_size_y)
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

#logo = pygame.image.load('katte.png')

maze = pygame.image.load('James_maze.png')

'''
<<<<<<< HEAD
=======
pygame.display.set_icon(logo)
>>>>>>> 8e3c981df09e543c2f409ae9642429473748450f
'''

# buttons
buttonObj = []
for x in range(0,10):
    for y in range(0,10):
        buttonObj.append(pygbutton.PygButton((x*50, y*50, 50, 50), ""))




# main game loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()
        for x in range(0, len(buttonObj)):
            if 'click' in buttonObj[x].handleEvent(event):
                pygame.quit()
                sys.exit()
                pass
    for e in buttonObj:
        e.draw(window)
    pygame.display.flip()

