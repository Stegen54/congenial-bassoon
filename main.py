import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle named "builder"
builder = turtle.Turtle()
builder.speed(2)

# Function to draw a square
def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Function to draw a triangle
def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Draw the base of the house
builder.penup()
builder.goto(-50, -50)
builder.pendown()
draw_square(builder, 100, "yellow")

# Draw the roof of the house
builder.penup()
builder.goto(-50, 50)
builder.pendown()
draw_triangle(builder, 100, "brown")

# Draw the door
builder.penup()
builder.goto(-15, -50)
builder.pendown()
draw_square(builder, 30, "blue")

# Draw windows
builder.penup()
builder.goto(-40, 0)
builder.pendown()
draw_square(builder, 20, "white")

builder.penup()
builder.goto(20, 0)
builder.pendown()
draw_square(builder, 20, "white")

# Hide the turtle and display the window
builder.hideturtle()
turtle.done()