from turtle import *
turtle = Turtle()
screen= Screen()
screen.bgcolor ("black")
turtle.pensize(3)
def dikdortgen_ciz (renk, dolgu, genislik, yukseklik):
    turtle.goto(0,0)
    turtle.color (renk)
    turtle.fillcolor (dolgu)
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(genislik)
        turtle.left (90)
        turtle. forward (yukseklik)
        turtle.left (90)
        turtle.end_fill()

dikdortgen_ciz("grey", "white", 200,120)