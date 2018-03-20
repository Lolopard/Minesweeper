import pygame, sys, time

from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

x_size=300

y_size=330

size = ( x_size , y_size )

board = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper Config")

font = pygame.font.SysFont('Comic Sans MS', 25, False, False)

bounce = pygame.image.load('windowz.png')

logo = pygame.image.load('katte.png')

maze = pygame.image.load('James_maze.png')

pygame.display.set_icon(logo)

'''
# fps counter #

y_origin = time.time()

x = 0
'''

# bouncing thing #

x_movement=4
y_movement=4

ay = 0+20
bx = 34+33
cy = 33+20
dx = 1+33

char_x=0
char_y=0

char_x_move=0
char_y_move=0

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            print("User asked to quit")
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if event.key == pygame.K_UP:
                print("User said up")
                char_y_move=-3

            elif event.key == pygame.K_DOWN:
                print("User said down")
                char_y_move=3

            elif event.key == pygame.K_RIGHT:
                 print("User said right")
                 char_x_move=3

            elif event.key == pygame.K_LEFT:
                print("User said left")
                char_x_move=-3

        elif event.type == KEYUP:

            char_x_move=0
            char_y_move=0

    ### Game logic ###
    '''
    # fps counter #
    
    x+=1
    y=time.time()-y_origin
    try:
        z=int(x/y)
    except ZeroDivisionError:
        z=0
    fps_text = font.render(str(z),True,(0,255,0))
    fps_text_2 = font.render(str(z),True,(0,200,0))
    '''
    # bouncing thing #

    if ay <= 0:

        y_movement=4

    elif bx >= x_size:

        x_movement=-4

    elif cy >= y_size:

        y_movement=-4

    elif dx <= 0:

        x_movement=4

    ay += y_movement
    bx += x_movement
    cy += y_movement
    dx += x_movement

    hitbox_x=dx
    hitbox_y=ay

    char_x+=char_x_move
    char_y+=char_y_move

    ### Graphics ###

    board.fill((255,255,255))

    pygame.draw.rect(board,(200,200,200),[0,0,x_size,y_size],3)

    pygame.draw.rect(board,(200,200,200),[0,0,x_size,30],0)

    pygame.draw.rect(board,(100,100,100),[1,1,x_size-1,y_size-1],1)

    pygame.draw.rect(board,(100,100,100),[1,29,x_size-2,1],1)

    board.blit(maze, (0, 0))
    
    '''
    board.blit(fps_text_2, [2, -2])

    board.blit(fps_text_2, [4, -4])

    board.blit(fps_text, [3, -3])
    '''
    #pygame.draw.rect(board,(0,255,127),[hitbox_x,hitbox_y,33,33],0)

    board.blit(bounce, (hitbox_x,hitbox_y))

    pygame.draw.rect(board,(0,255,12),[char_x,char_y,33,33],0)
    
    ### Render ###

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

