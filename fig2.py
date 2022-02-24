#import matplotlib.pyplot as plt
import turtle 

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)

turtle.penup()
turtle.goto(-350,100)
turtle.pendown()
turtle.color("green")

for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()


