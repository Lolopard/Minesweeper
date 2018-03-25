import pygame, sys, time
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

window_size_x = 500
window_size_y = 500

window_size = (window_size_x, window_size_y)
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

logo = pygame.image.load('katte.png')

maze = pygame.image.load('James_maze.png')

<<<<<<< HEAD
=======
pygame.display.set_icon(logo)
>>>>>>> 8e3c981df09e543c2f409ae9642429473748450f
