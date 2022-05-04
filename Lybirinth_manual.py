from numpy import insert, true_divide


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
    


def move(step, current_position_x, current_position_y):
    print("Current step is: ", step)
    print("Current current_position_y =",current_position_y)
    print("Current current_position_x =",current_position_x)
    for i in map:  # Вывод мапы
        print(i)

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

    if(where == "up"):
        can_move_top = current_position_y >= 1 and map[current_position_y-1][current_position_x] == 0
    
    if(where == "down"):
        can_move_bottom = current_position_y <= 4 and map[current_position_y+1][current_position_x] == 0 
    
    if(where == "right"):
        can_move_right = current_position_x <= 4 and map[current_position_y][current_position_x+1] == 0
    
    if(where == "left"):
        can_move_left = current_position_x >= 1 and map[current_position_y][current_position_x-1] == 0
        

current_move_number = 1
new_position = move(current_move_number, start_position_x, start_position_y)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1])