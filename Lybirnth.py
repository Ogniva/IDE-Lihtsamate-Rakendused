
from hashlib import new
import random

map1=[
    [12,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,0,24]
]

map2=[
    [12,1,0,0],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,0,24]
]

map3=[
    [12,1,0,0],
    [0,0,1,0],
    [1,0,1,0],
    [24,0,0,0]
]

map4=[
    [12,0,1,0,0,0],
    [1,0,1,0,0,0],
    [1,0,1,0,1,1],
    [0,0,1,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,0,24]
]

map=map4

# Start position

start_position_x = 0
start_position_y = 0

can_move_rigth = 0
can_move_left = 0
# Steps

def move(step, current_position_x, current_position_y):
    print("Current step is: ", step)
    print("Current current_position_y =",current_position_y)
    print("Current current_position_x =",current_position_x)
    
    can_move_right = current_position_x <= 4 and map[current_position_y][current_position_x+1] == 0
    can_move_left = current_position_x >= 1 and map[current_position_y][current_position_x-1] == 0
    can_move_bottom = current_position_y <= 4 and map[current_position_y+1][current_position_x] == 0 
#    can_move_top = current_position_y >= 0 and map[current_position_y-1][current_position_x] == 0

    right_is_finish = current_position_x <= 4 and map[current_position_y][current_position_x+1] == 24
    bottom_is_finish = current_position_y <= 4 and map[current_position_y+1][current_position_x] == 24
    left_is_finish = current_position_x >= 1 and map[current_position_y][current_position_x-1] == 24
#    top_is_finish = current_position_y >= 0 and map[current_position_y-1][current_position_x] == 24

    if right_is_finish:
        print("Found finish on right")
        return False
    if bottom_is_finish:
        print("Found finish on bottom")  
        return False
    if left_is_finish:
        print("Found finish on left")
        return False

    
    if can_move_bottom:
        print("Should move down")
        return [current_position_x, current_position_y + 1]
    while not right_is_finish or not bottom_is_finish or not left_is_finish:
        if random.random() > 0.5:
            if can_move_right:
                print("Should move right")
                return [current_position_x + 1, current_position_y]
        elif random.random() < 0.5:
            if can_move_left:
                print("Should move left")
                return [current_position_x - 1, current_position_y]


#new_position = move(1, start_position_x, start_position_y)
#new_position = move(2, new_position[0], new_position[1])
#new_position = move(3, new_position[0], new_position[1])
#new_position = move(4, new_position[0], new_position[1])
#new_position = move(5, new_position[0], new_position[1])
#new_position = move(6, new_position[0], new_position[1])
#new_position = move(7, new_position[0], new_position[1])
#new_position = move(8, new_position[0], new_position[1])

current_move_number = 1
new_position = move(current_move_number, start_position_x, start_position_y)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1])

