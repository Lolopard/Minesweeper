import pygame
import sys
import time
from pygame.locals import *
from minesweeper_functions import *

pygame.init()

clock = pygame.time.Clock()

font = pygame.font.SysFont("Comic Sans MS", 22, False, False)

window = pygame.display.set_mode([320, 240])

pygame.display.set_caption("Launch Options")

pygame.display.set_icon(pygame.image.load('settingsicon.png'))

# OPTIONS MENU

adv = False
done = False

x_type = pygame.Rect(140, 90, 60, 30)
y_type = pygame.Rect(140, 90 + 45, 60, 30)
m_type = pygame.Rect(140, 90 + 90, 90, 30)

x_active = False
y_active = False
m_active = False

x_string = ""
y_string = ""
m_string = "0.0"

x_colour = [70, 70, 70]
y_colour = [70, 70, 70]
m_colour = [70, 70, 70]
    
while done is False:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()
        if 'click' in option_buttons[0].handleEvent(event) and adv is False:
            # Easy
            squares_y = 24
            squares_x = 20
            mine_ratio = 0.18
            done = True
        elif 'click' in option_buttons[1].handleEvent(event) and adv is False:
            # Medium
            squares_y = 28
            squares_x = 24
            mine_ratio = 0.2
            done = True
        elif 'click' in option_buttons[2].handleEvent(event) and adv is False:
            # Hard
            squares_y = 32
            squares_x = 28
            mine_ratio = 0.22
            done = True
        elif 'click' in option_buttons[3].handleEvent(event) and adv is False:
            adv = True
            custom = False
        elif 'click' in adv_option_buttons[0].handleEvent(event) and adv is True:
            adv = False
        elif 'click' in adv_option_buttons[1].handleEvent(event) and adv is True and custom is True:
            # Translates the typing fields into the different variables
            squares_y = int(y_string)
            squares_x = int(x_string)
            mine_ratio = float(m_string)
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and adv is True:
            if x_type.collidepoint(event.pos):
                x_active, y_active, m_active = True, False, False
                x_colour, y_colour, m_colour = [0, 0, 0], [70, 70, 70], [70, 70, 70]
            elif y_type.collidepoint(event.pos):
                x_active, y_active, m_active = False, True, False
                x_colour, y_colour, m_colour = [70, 70, 70], [0, 0, 0], [70, 70, 70]
            elif m_type.collidepoint(event.pos):
                x_active, y_active, m_active = False, False, True
                x_colour, y_colour, m_colour = [70, 70, 70], [70, 70, 70], [0, 0, 0]
            else:
                x_active = y_active = m_active = False
                x_colour = y_colour = m_colour = [70, 70, 70]                
        elif event.type == pygame.KEYDOWN and x_active is True:
            if event.key == pygame.K_BACKSPACE:
                x_string = x_string[:-1]
            elif len(x_string) < 3:
                x_string += event.unicode
        elif event.type == pygame.KEYDOWN and y_active is True:
            if event.key == pygame.K_BACKSPACE:
                y_string = y_string[:-1]
            elif len(y_string) < 3:
                y_string += event.unicode
        elif event.type == pygame.KEYDOWN and m_active is True:
            if event.key == pygame.K_BACKSPACE and len(m_string) > 3:
                m_string = m_string[:-1]
            elif len(m_string) < 6:
                m_string += event.unicode

    x_text = font.render(x_string, True, [255, 255, 255])
    y_text = font.render(y_string, True, [255, 255, 255])
    m_text = font.render(m_string, True, [255, 255, 255])

    try:
        if int(x_string) != 0 and int(y_string) != 0 and float(m_string) != 0:
            custom = True
        else:
            custom = False
    except:
        custom = False
        
    window.fill([192, 192, 192])
    if adv is False:
        for b in range(4):
            option_buttons[b].draw(window)
    else:
        adv_option_buttons[0].draw(window)
        # TYPING FIELDS #
        pygame.draw.rect(window, x_colour, x_type, 0)
        pygame.draw.rect(window, y_colour, y_type, 0)
        pygame.draw.rect(window, m_colour, m_type, 0)
        window.blit(x_text, (150, 89))
        window.blit(y_text, (150, 134))
        window.blit(m_text, (150, 179))
        if custom is True:
            adv_option_buttons[1].draw(window)
    pygame.display.flip()
    if done is True:
        pygame.quit()

pygame.init()
font = pygame.font.SysFont("Comic Sans MS", 22, False, False)

square_size = 16  # length of side of square in pixels

# Stuff to put into options menu
'''
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
'''

window_size = (squares_y * square_size, squares_x * square_size + 48)

window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Minesweeper")
'''
font = pygame.font.SysFont('Comic Sans MS', 25, False, False)
'''
logo = pygame.image.load('icon.png')

face = pygame.image.load("face.png")
face_lose = pygame.image.load("face_lose.png")
face_win = pygame.image.load("face_win.png")

picture_list = []
for x in range(0, 9):
    picture_list.append(pygame.image.load(str(x) + ".png"))

picture_list.append(pygame.image.load("mine.png"))

picture_list.append(pygame.image.load("mine_blow.png"))

pygame.display.set_icon(logo)

window.fill([192, 192, 192])

minefield = generate_blank(squares_y, squares_x)
# Placeholder field until the real is generated ( So the graphics work )

generated_buttons = generate_buttons(squares_y, squares_x, square_size)
field_buttons = generated_buttons[0]
clicked_buttons = generated_buttons[1]

restart_button = pygbutton.PygButton((window_size[0]/2 - 16, 8, 32, 32), "")

game_state = "playing"

first_click = False

time_start = time.clock()

time_elapsed = 0

timer_on = True

# main game loop
while True:
    window.fill([192, 192, 192])
    if game_state == "playing":
        time_elapsed = round(time.clock() - time_start)
    for event in pygame.event.get():
        restart_button.draw(window)
        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()
        if game_state == "playing": # If you win or lose, you can't play
            for x in range(0, squares_x):
                for y in range(0, squares_y):
                    if first_click is True:
                        if 'click' in field_buttons[y][x].handleEvent(event) and clicked_buttons[y][x] is False:
                            clicked_buttons[y][x] = True
                            if minefield[y][x] == mine:
                                game_state = "lost"
                                print("You lost")
                                loss_clear(x, y, minefield, clicked_buttons, squares_x, squares_y)
                            elif minefield[y][x] == 0:
                                big_clear(x, y, minefield, clicked_buttons, squares_x, squares_y)    
                                if win_check(minefield, clicked_buttons, squares_x, squares_y) is True:
                                    game_state = "won"
                                    print("You won")
                            else:
                                if win_check(minefield, clicked_buttons, squares_x, squares_y) is True:
                                    game_state = "won"
                                    print("You won")

                    else:
                        if 'click' in field_buttons[y][x].handleEvent(event):
                            first_click = True
                            minefield = generate_board(squares_y, squares_x, x, y, mine_ratio)
                            clicked_buttons[y][x] = True
                            if minefield[y][x] == 0:
                                big_clear(x, y, minefield, clicked_buttons, squares_x, squares_y)    
                                if win_check(minefield, clicked_buttons, squares_x, squares_y) is True:
                                    game_state = "won"
                                    print("You won")
    if game_state == "playing":
        window.blit(face, (window_size[0] / 2 - 16, 8))

    elif game_state == "lost":
        window.blit(face_lose, (window_size[0] / 2 - 16, 8))

    elif game_state == "won":
        window.blit(face_win, (window_size[0] / 2 - 16, 8))

    if "click" in restart_button.handleEvent(event):
        generated_buttons = generate_buttons(squares_y, squares_x, square_size)
        field_buttons = generated_buttons[0]
        clicked_buttons = generated_buttons[1]
        minefield = generate_board(squares_y, squares_x, x, y, mine_ratio)
        first_click = False
        game_state = "playing"
        time_start = time.clock()

    time_display = font.render(str(time_elapsed), 1, (0, 0, 0))
    window.blit(time_display, (0, 0))
            
    for x in range(0, squares_x):
        for y in range(0, squares_y):
            if clicked_buttons[y][x] is False:
                field_buttons[y][x].draw(window)
            else:
                if isinstance(minefield[y][x], int):
                    window.blit(picture_list[minefield[y][x]], (y * square_size, x * square_size + 48))
                elif minefield[y][x] == mine:
                    window.blit(picture_list[9], (y * square_size, x * square_size + 48))
                elif minefield[y][x] == mine_blow:
                    window.blit(picture_list[10], (y * square_size, x * square_size + 48))
    clock.tick(60)
    pygame.display.flip()
