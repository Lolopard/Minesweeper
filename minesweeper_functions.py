import random


def generate_board(length_x, length_y, origin_x, origin_y, mine_ratio):
    global minefield
    global empty
    global mine
    global border
    
    minefield = []

    empty = 0

    mine = 'mine.png'

    border = 9  # could any int, idk. maybe will be changed to 0 if memory is an issue

    mine_count = int(length_x * length_y * mine_ratio)

    for x in range(length_x + 2):
        minefield.append([])
        for y in range(length_y + 2):
            if x == 0 or x == (length_x + 1) or y == 0 or y == (length_y + 1):
                minefield[x].append(border)
            else:
                minefield[x].append(empty)

    for mines in range(mine_count):
        
        reroll = True
        while reroll:
            reroll = False  # In case of a overlap
            
            mine_pos_x = random.randint(1, (length_x))  # initial roll
            mine_pos_y = random.randint(1, (length_y))
            
            if mine_pos_x == origin_x and mine_pos_y == origin_y:
                reroll = True
                
            elif minefield[mine_pos_x][mine_pos_y] == mine:
                reroll = True  # reroll for overlap
                
        for x_modifier in range(-1, 2):
            for y_modifier in range(-1, 2):
                if minefield[mine_pos_x + x_modifier][mine_pos_y + y_modifier] != mine:
                    minefield[mine_pos_x + x_modifier][mine_pos_y + y_modifier] += 1
        minefield[mine_pos_x][mine_pos_y] = mine

    # strips the border, only useful for preventing index errors
    minefield.pop(0)
    minefield.pop(-1)
    for x in range (0, length_y):
        minefield[x].pop(0)
        minefield[x].pop(-1)


generate_board(20, 20, 1, 1, 0.1)
print(minefield)


def print_board():
    for l in minefield:
        for e in l:
            if e == 'mine.png':
                print("*", end=" ")
            else:
                print(e, end=" ")
        print()


print_board()
