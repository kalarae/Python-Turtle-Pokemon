#-----------------------------------+
# Michaela Lightner                 |
# CSCI 107, Assignment 3            |
# Last Updated: September 21, 2016  |
#-----------------------------------|
# This program provides a simple    |
# python turtle image of a Pokemon. |
#-----------------------------------+

import turtle

window = turtle.Screen()
window.bgcolor("gainsboro")

oddish = turtle.Turtle()
oddish.speed(0)
oddish.penup()
oddish.goto(0, -50)
oddish.pendown()
oddish.begin_fill()

oddish.color("black", "midnightblue")        #body
oddish.circle(50)
oddish.end_fill()
oddish.penup()

oddish.goto(-30, -40)               #feet
oddish.pendown()
oddish.right(45)
oddish.begin_fill()

oddish.right(90)                    #left foot
oddish.circle(10, 230)
oddish.end_fill()

oddish.begin_fill()                 #beginning right foot
oddish.penup()
oddish.goto(20, -45)
oddish.pendown()
oddish.right(180)
oddish.circle(10, 250)
oddish.end_fill()

oddish.penup()                          #the mouth
oddish.goto(-15, -10)
oddish.left(105)
oddish.pendown()
oddish.color("black", "salmon")
oddish.begin_fill()
oddish.circle(15, 180)
oddish.left(90)
oddish.forward(30)
oddish.end_fill()

oddish.penup()                           #left eye
oddish.goto(-10, 10)
oddish.pendown()
oddish.right(90)
oddish.color("black")
oddish.begin_fill()
oddish.circle(8)
oddish.end_fill()

oddish.penup()
oddish.circle(8, 160)
oddish.pendown()
oddish.color("white")
oddish.begin_fill()
oddish.circle(3)
oddish.end_fill()

oddish.penup()                           #right eye
oddish.goto(12, 10)
oddish.left(20)
oddish.pendown()
oddish.color("black")
oddish.begin_fill()
oddish.circle(8)
oddish.end_fill()

oddish.penup()
oddish.circle(8, -20)
oddish.pendown()
oddish.color("white")
oddish.begin_fill()
oddish.circle(3)
oddish.end_fill()

oddish.penup()                          #leaves
oddish.goto(-25, 35)
oddish.pendown()
oddish.color("black", "green")
oddish.begin_fill()
oddish.left(180)
oddish.circle(50, 130)
oddish.end_fill()

oddish.left(50)
oddish.color("black", "lawngreen")
oddish.begin_fill()
oddish.circle(50, 130)
oddish.end_fill()

oddish.penup()
oddish.goto(-10, 40)
oddish.pendown()
oddish.right(10)
oddish.color("black", "green")
oddish.begin_fill()
oddish.circle(50, 130)
oddish.end_fill()

oddish.left(50)
oddish.color("black", "lawngreen")
oddish.begin_fill()
oddish.circle(50, 130)
oddish.end_fill()

oddish.penup()
oddish.goto(20, 35)
oddish.pendown()
oddish.left(20)
oddish.color("black", "green")
oddish.begin_fill()
oddish.circle(50, 130)
oddish.end_fill()

oddish.left(50)
oddish.color("black", "lawngreen")
oddish.begin_fill()
oddish.circle(50, 130)
oddish.end_fill()

oddish.hideturtle()
window.exitonclick()
