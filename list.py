from turtle import*
from colorsys import*
from math import*
bgcolor("black")
width(1)
speed(0)
hideturtle()
for i in range(300):
    i = int(h * 6.0)
    r=(i * 3) % 245
    g=(i * 4) % 245
    b=(i * 5)% 245
    color(hsv_to_rgb(h,1,1))
    h=+1/3
    pencolor("violet")
    left(121)
    forward(i * 1.2)
done()
