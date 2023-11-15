import turtle
import random

def generate_random_name():
    names = ["Angel aka ochy"]
    return random.choice(names)

screen = turtle.Screen()
screen.bgcolor("white")

heart_turtle = turtle.Turtle()
heart_turtle.shape("turtle")
heart_turtle.color("red")

heart_turtle.penup()
heart_turtle.goto(0, -200)
heart_turtle.pendown()

def draw_heart():
    heart_turtle.begin_fill()
    heart_turtle.left(50)
    heart_turtle.forward(133)
    heart_turtle.circle(50, 200)
    heart_turtle.right(140)
    heart_turtle.circle(50, 200)
    heart_turtle.forward(133)
    heart_turtle.end_fill()

draw_heart()

name = generate_random_name()
font_style = ("Arial", 12, "normal")
heart_turtle.penup()
heart_turtle.goto(0, -220)
heart_turtle.color("black")
heart_turtle.write(name, align="center", font=font_style)

heart_turtle.hideturtle()

turtle.done()
