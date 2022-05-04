
map4=[
    [12,0,1,0,0,0],
    [1,0,1,0,0,0],
    [1,0,1,0,1,1],
    [0,0,1,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,0,24]
]

map=map4
    
#------Start----------

start_position_x = 0
start_position_y = 0

can_move_rigth = 0
can_move_left = 0

#--------------------

for i in map:  # Вывод мапы
    print(i)

Ready = input("You are ready? ")
if(Ready == "Yes" or Ready == "yes" or Ready == "ye"):
    print("start")
else:
    print("OOOOOOOKAAAAAAY next time")
    exit()
    


def move(step, current_position_x, current_position_y, where):
    print("Current step is: ", step)
    print("Current current_position_y =",current_position_y)
    print("Current current_position_x =",current_position_x)
    
    for i in map:  # Вывод мапы
        print(i)

    right_is_finish = current_position_x <= 4 and map[current_position_y][current_position_x+1] == 24
    bottom_is_finish = current_position_y <= 4 and map[current_position_y+1][current_position_x] == 24
    left_is_finish = current_position_x >= 1 and map[current_position_y][current_position_x-1] == 24
    top_is_finish = current_position_y >= 1 and map[current_position_y-1][current_position_x] == 24

    if right_is_finish:
        print("Found finish on right ")
        return False
    if bottom_is_finish:
        print("Found finish on bottom ")  
        return False
    if left_is_finish:
        print("Found finish on left ")
        return False
    if top_is_finish:
        print("Found finish on left ")
        return False

    can_move_up = where == "up" and current_position_y >= 1 and map[current_position_y-1][current_position_x] == 0
    can_move_down = where == "down" and current_position_y <= 4 and map[current_position_y+1][current_position_x] == 0 
    can_move_right = where == "right" and current_position_x <= 4 and map[current_position_y][current_position_x+1] == 0
    can_move_left = where == "left" and current_position_x >= 1 and map[current_position_y][current_position_x-1] == 0

    if (can_move_up == True):
        print("Should move up")
        current_position_x = current_position_x + 1
    if (can_move_down == True):
        print("Should move down")
        current_position_y = current_position_y + 1
    if (can_move_left  == True):
        print("Should move left")
        current_position_x = current_position_x + 1
    if (can_move_right == True):
        print("Should move down right")
        current_position_y = current_position_y + 1

current_move_number = 1
where = input("up down right left?")
word = "GG"
while(word == "GG"):
    if(where == "up"):
        word = where
    elif(where == "down"):
        word = where
    elif(where == "right"):
         word = where
    elif(where == "left"):
        word = where
    else:
        word = "GG"
        where = input("up down right left?")

new_position = move(current_move_number, start_position_x, start_position_y, where)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1], where)