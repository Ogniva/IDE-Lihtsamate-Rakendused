from turtle import *

setpos(300,100)
speed(20)
color('red')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
done()