import pygame, sys, time
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

x_size = 300

y_size = 330

size = (x_size, y_size)

board = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper Config")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

bounce = pygame.image.load('windowz.png')

maze = pygame.image.load('James_maze.png')

pygame.display.set_icon(bounce)


# fps counter/mouse pos #

y_origin = time.time()

x = 0


# bouncing thing #

x_movement = 4
y_movement = 4

top_face = 0 + 20
right_face = 34 + 33
bottom_face = 33 + 20
left_face = 1 + 33

char_pos_x = 0
char_pos_y = 0

char_move_x = 0
char_move_y = 0

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if event.key == pygame.K_UP:
                print("User said up")
                char_move_y=-3

            elif event.key == pygame.K_DOWN:
                print("User said down")
                char_move_y=3

            elif event.key == pygame.K_RIGHT:
                 print("User said right")
                 char_move_x=3

            elif event.key == pygame.K_LEFT:
                print("User said left")
                char_move_x=-3

        elif event.type == KEYUP:

            char_move_x=0
            char_move_y=0

    ### Game logic ###

    # fps counter/mouse pos #

    x += 1
    y = time.time() - y_origin
    try:
        z = int(x/y)
    except ZeroDivisionError:
        z = 0
    fps_text = font.render(str(pygame.mouse.get_pos()), True, (0, 255, 0))
    fps_text_2 = font.render(str(pygame.mouse.get_pos()), True, (0, 200, 0))

    # bouncing thing #

    if top_face <= 0:

        y_movement = 4

    elif right_face >= x_size:

        x_movement = -4

    elif bottom_face >= y_size:

        y_movement=  -4

    elif left_face <= 0:

        x_movement = 4

    top_face += y_movement
    right_face += x_movement
    bottom_face += y_movement
    left_face += x_movement

    hitbox_x = left_face
    hitbox_y = top_face

    char_pos_x += char_move_x
    char_pos_y += char_move_y

    ### Graphics ###

    board.fill((255,255,255))

    pygame.draw.rect(board, (200, 200, 200), [0, 0, x_size, y_size], 3)

    pygame.draw.rect(board, (200, 200, 200), [0, 0, x_size, 30], 0)

    pygame.draw.rect(board,  (100, 100, 100), [1, 1, x_size-1, y_size-1], 1)

    pygame.draw.rect(board,(100, 100, 100), [1, 29, x_size-2, 1], 1)

    board.blit(maze, (0, 0))
    

    board.blit(fps_text_2, [2, -2])

    board.blit(fps_text_2, [4, -4])

    board.blit(fps_text, [3, -3])

    #pygame.draw.rect(board,(0,255,127),[hitbox_x,hitbox_y,33,33],0)

    board.blit(bounce, (hitbox_x, hitbox_y))

    pygame.draw.rect(board, (0, 255, 12), [char_pos_x, char_pos_y, 33, 33], 0)
    
    ### Render ###

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

