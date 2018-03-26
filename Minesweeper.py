import pygame
import sys
import time
import pygbutton
from pygame.locals import *
from minesweeper_functions import *

clock = pygame.time.Clock()

pygame.init()

square_size = 20  # length of side of square in pixels

print("Choose size of board (press enter without an input for default)")
squares_x = (input("Number of squares in x axis: "))
squares_y = (input("Number of squares in y axis: "))

if squares_x == "" and squares_y == "":
    squares_x = 20
    squares_y = 20
else:
    squares_x = int(squares_x)
    squares_y = int(squares_y)

window_size = (squares_x * square_size, squares_y * square_size)

window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

#logo = pygame.image.load('katte.png')

picture = pygame.image.load("goface.jpg")

'''
<<<<<<< HEAD
=======
pygame.display.set_icon(logo)
>>>>>>> 8e3c981df09e543c2f409ae9642429473748450f
'''

# buttons
field_buttons = []
clicked_buttons = []
for x in range(0, squares_x):
    button_row = []
    clicked_button_row = []
    for y in range(0, squares_y):
        button_row.append(pygbutton.PygButton((x * square_size, y * square_size, square_size, square_size), ""))
        clicked_button_row.append(False)
    field_buttons.append(button_row)
    clicked_buttons.append(clicked_button_row)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()
        for x in range(0, squares_x):
            for y in range(0, squares_y):
                if 'click' in field_buttons[y][x].handleEvent(event) and clicked_buttons[y][x] is False:
                    clicked_buttons[y][x] = True
                    #pygame.quit()
                    #sys.exit()
                    pass
    for x in range(0, squares_x):
        for y in range(0, squares_y):
            if clicked_buttons[y][x] == False:
                field_buttons[y][x].draw(window)
    pygame.display.flip()
    window.blit(picture, (0, 0))
