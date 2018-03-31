import pygame
import sys
import time
import pygbutton
from pygame.locals import *
from minesweeper_functions import *

clock = pygame.time.Clock()

pygame.init()

square_size = 16  # length of side of square in pixels

print("Choose board settings (press enter without an input for default)")
squares_x = (input("Number of squares in x axis: "))
squares_y = (input("Number of squares in y axis: "))
mine_ratio = (input("Ratio of mines to squares: "))

if squares_x == "" and squares_y == "" and mine_ratio == "":
    squares_x = 20
    squares_y = 20
    mine_ratio = 0.1
else:
    squares_x = int(squares_x)
    squares_y = int(squares_y)
    mine_ratio = int(mine_ratio)


window_size = (squares_x * square_size, squares_y * square_size)

window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

#logo = pygame.image.load('katte.png')

picture = pygame.image.load("goface.jpg")

picture_list = []
for x in range(0, 9):
    picture_list.append(pygame.image.load(str(x) + ".png"))

picture_list.append(pygame.image.load("mine.png"))

print(picture_list)

'''
<<<<<<< HEAD
=======
pygame.display.set_icon(logo)
>>>>>>> 8e3c981df09e543c2f409ae9642429473748450f
'''

minefield = generate_board(squares_x, squares_y, 0, 0, 0.1)

print_board(minefield)

generated_buttons = generate_buttons(squares_x, squares_y, square_size)
field_buttons = generated_buttons[0]
clicked_buttons = generated_buttons[1]

squares_clicked = 0

game_state = None

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
                    '''
                    if minefield[y][x] == mine:
                        game_state = "loss"  # lost game, all squares open
                    elif minefield[y][x] == 0:
                        # big_clear + win check
                        pass
                    else:
                        # win check
                        squares_clicked += 1
                        if squares_clicked == (squares_x * squares_y) * (1 - mine_ratio):
                            game_state = "win"  # won game, all squares open
                    #pygame.quit()
                    #sys.exit()
                    '''
                    pass

    if game_state is not None:
        pass



    for x in range(0, squares_x):
        for y in range(0, squares_y):
            if clicked_buttons[y][x] is False:
                field_buttons[y][x].draw(window)
            else:
                if isinstance(minefield[y][x], int):
                    window.blit(picture_list[minefield[y][x]], (y * square_size, x * square_size))
                    if minefield[y][x] == 0:
                        #big_clear(x, y, squares_x, squares_y, minefield, clicked_buttons)
                        pass
                elif minefield[y][x] == mine:
                    window.blit(picture_list[9], (y * square_size, x * square_size))
    pygame.display.flip()
