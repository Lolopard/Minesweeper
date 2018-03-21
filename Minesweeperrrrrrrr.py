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

bounce = pygame.image.load('windowz.png')

maze = pygame.image.load('James_maze.png')

pygame.display.set_icon(bounce)