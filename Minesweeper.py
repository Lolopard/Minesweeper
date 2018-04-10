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
squares_y = (input("Number of squares in x axis: "))
squares_x = (input("Number of squares in y axis: "))
mine_ratio = (input("Ratio of mines to squares: "))

if squares_y == "" and squares_x == "" and mine_ratio == "":
    squares_y = 20
    squares_x = 20
    mine_ratio = 0.1
else:
    squares_y = int(squares_y)
    squares_x = int(squares_x)
    mine_ratio = float(mine_ratio)


window_size = (squares_y * square_size, squares_x * square_size)

window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

logo = pygame.image.load('icon.png')

picture_list = []
for x in range(0, 9):
    picture_list.append(pygame.image.load(str(x) + ".png"))

picture_list.append(pygame.image.load("mine.png"))

picture_list.append(pygame.image.load("mine_blow.png"))

pygame.display.set_icon(logo)

minefield = generate_board(squares_y, squares_x, 0, 0, mine_ratio)
# Needs to be moved into the loop for the first click 

print_board(minefield)

generated_buttons = generate_buttons(squares_y, squares_x, square_size)
field_buttons = generated_buttons[0]
clicked_buttons = generated_buttons[1]

squares_clicked = 0 # Dont need this anymore

game_state = None

first_click = False

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()
        if game_state is None: # If you win or lose, you can't play
            for x in range(0, squares_x):
                for y in range(0, squares_y):
                    if 'click' in field_buttons[y][x].handleEvent(event) and clicked_buttons[y][x] is False:
                        clicked_buttons[y][x] = True
                        if minefield[y][x] == mine:
                            game_state = False
                            print("You lost")
                            loss_clear(x, y, minefield, clicked_buttons, squares_x, squares_y)
                        elif minefield[y][x] == 0:
                            big_clear(x, y, minefield, clicked_buttons, squares_x, squares_y)    
                            if win_check(minefield, clicked_buttons, squares_x, squares_y) is True:
                                game_state = True
                                print("You won")
                        else:
                            if win_check(minefield, clicked_buttons, squares_x, squares_y) is True:
                                game_state = True
                                print("You won")
                        '''
                        if minefield[y][x] == mine:
                            game_state = "loss"  # lost game, all squares open
                        elif minefield[y][x] == 0:
                            # big_clear + win check
                            pass
                        else:
                            # win check
                            squares_clicked += 1
                            if squares_clicked == (squares_y * squares_x) * (1 - mine_ratio):
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
                elif minefield[y][x] == mine:
                    window.blit(picture_list[9], (y * square_size, x * square_size))
                elif minefield[y][x] == mine_blow:
                    window.blit(picture_list[10], (y * square_size, x * square_size))
    pygame.display.flip()

    
