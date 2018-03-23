import random

def generate_board ( x_length , y_length , origin_x , origin_y , mine_ratio ):

    global minefield
    global empty
    global mine
    global boarder
    
    minefield = []

    empty = " "

    mine = 'mine.png'

    boarder = "shiz"

    mine_count = int( x_length * y_length * mine_ratio )

    for x in range(x_length+2):
        minefield.append([])
        for y in range(y_length+2):
            if x == 0 or x == (x_length+1) or y == 0 or y == (y_length+1):
                minefield[x].append(boarder)
            else:
                minefield[x].append(empty)

    for mines in range(mine_count):
        mine_pos_x=random.randint(0,(x_length-1))
        mine_pos_y=random.randint(0,(y_length-1))
        while mine_pos_x == origin_x:
            mine_pos_x=random.randint(0,(x_length-1))
        while mine_pos_y == origin_y:
            mine_pos_y=random.randint(0,(y_length-1))
        minefield[mine_pos_x][mine_pos_y] = mine   #add numbers around

            
