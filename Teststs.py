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
print(where)