import random
import pygbutton

# unicode characters

mine = "*"
mine_blow = "#"


# outputs a field with generated mines and accompanying number squares
def generate_board(length_x, length_y, origin_x, origin_y, mine_ratio):
    minefield = []

    empty = 0

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
                
        for modifier_x in range(-1, 2):
            for modifier_y in range(-1, 2):
                if minefield[mine_pos_x + modifier_x][mine_pos_y + modifier_y] != mine:
                    minefield[mine_pos_x + modifier_x][mine_pos_y + modifier_y] += 1
        minefield[mine_pos_x][mine_pos_y] = mine

    # strips the border which is only useful for preventing index errors
    
    minefield.pop(0)
    minefield.pop(-1)
    for x in range(0, length_x):
        minefield[x].pop(0)
        minefield[x].pop(-1)
        

    return minefield

def generate_blank(length_x, length_y):
    minefield = []
    
    for x in range(length_x + 2):
        minefield.append([])
        for y in range(length_y + 2):
            minefield[x].append(mine)

    return minefield

def print_board(minefield):
    for l in minefield:
        for e in l:
            if e == mine:
                print("*", end=" ")
            else:
                print(e, end=" ")
        print()


# buttons and clicked grid
# outputs a list with a field of buttons as element 0 and list with a field of booleans as element 1
def generate_buttons(squares_x, squares_y, square_size):
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
    return [field_buttons, clicked_buttons]


'''
# trash, fix as soon as possible
def big_clear(x, y, minefield, clicked_buttons):
    operation_list = [(x, y)]
    checked_list = []
    while len(operation_list) > 0:
        if minefield[operation_list[0][1]][operation_list[0][0]] == 0 and operation_list[0] not in checked_list:
            clicked_buttons[operation_list[0][1]][operation_list[0][0]] = True
            checked_list.append(operation_list[0])
            for modifier_x in range(-1, 2):
                for modifier_y in range(-1, 2):
                    if minefield[operation_list[0][1] + modifier_y][operation_list[0][0] + modifier_x] == 0 and operation_list[0] not in checked_list:
                        operation_list.append(operation_list[0][0] + modifier_x, operation_list[0][1] + modifier_y)
                        checked_list.append(operation_list[0])
                        clicked_buttons[operation_list[0][1] + modifier_y][operation_list[0][0] + modifier_x]
                operation_list.pop(0)
'''

# let's try again

'''
def big_clear(x, y, length_x, length_y, minefield, clicked_buttons):
    op_list = [(x, y)]  # operation list, list of squares to check for zeroes
    checked_list = []  # list of squares already checked
    while len(op_list) > 0:
        inter_y = op_list[0][1]  # intermediate y, intermediate value for less typing
        inter_x = op_list[0][0]  # intermediate x, same as above
        if minefield[inter_y][inter_x] == 0:
            clicked_buttons[inter_y][inter_x] = True
            checked_list.append(op_list[0])
        for modifier_x in range(-1, 2):
            for modifier_y in range(-1, 2):
                if 0 <= (inter_y and inter_y <= length_y and inter_x >= 0 and inter_x <= length_x:
                    if minefield[inter_y + modifier_y][inter_x + modifier_x] == 0 and (inter_x + modifier_x, inter_y + modifier_y) not in checked_list:
                        op_list.append((inter_x + modifier_x, inter_y + modifier_y))
        op_list.pop(0)
'''
# I have failed twice

# let's try with Jimbob
# it kinda doesnt work
# I dont know why

def big_clear(x, y, minefield, clicked_buttons, length_x, length_y):
    operation = [[x, y]]
    while len(operation) > 0:
        for modifier_x in range(-1, 2):
            for modifier_y in range(-1, 2):
                    new_x = operation[0][0] + modifier_x
                    new_y = operation[0][1] + modifier_y
                    if new_x < length_x and new_y < length_y and new_x > -1 and new_y > -1:
                        clicked_buttons[new_y][new_x] = True
                        for ext_modifier_x in range(-1, 2):
                            for ext_modifier_y in range(-1, 2):
                                if (new_x + ext_modifier_x) < length_x and (new_y + ext_modifier_y) < length_y and (new_x + ext_modifier_x) > -1 and (new_y + ext_modifier_y) > -1:
                                    if clicked_buttons[new_y + ext_modifier_y][new_x + ext_modifier_x] is False and minefield[new_y][new_x] == 0:
                                        if [new_x, new_y] not in operation:
                                            operation.append([new_x, new_y])
                                else:
                                    pass
                    else:
                        pass
        operation.pop(0)

def loss_clear(loss_x, loss_y, minefield, clicked_buttons, length_x, length_y):
    for x in range(0, (length_x)):
        for y in range(0, (length_y)):
            if minefield[y][x] == mine:
                clicked_buttons[y][x] = True
    minefield[loss_y][loss_x] = mine_blow
    # Add red crosses over tiles that were false flagged
    # keep flags that are over bombs (dont show bombs)

def win_check(minefield, clicked_buttons, length_x, length_y):
    for x in range(0, (length_x)):
        for y in range(0, (length_y)):
            if clicked_buttons[y][x] is False and minefield[y][x] != mine:
                return False
    return True

            
    




