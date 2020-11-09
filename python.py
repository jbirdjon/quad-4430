import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("blue")
    square()
    rectangle()
    rhombus()
    parallelogram()
    window.exitonclick()

def square():
    t = turtle.Turtle()
    t.setheading(90)
    t.forward(100)
    t.setheading(180)
    t.forward(100)
    t.setheading(270)
    t.forward(100)
    t.setheading(360)
    t.forward(100)


def rectangle():
    t = turtle.Turtle()
    t.color("blue")
    t.goto(0,-100)
    t.color("black")
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(100)
    t.setheading(270)
    t.forward(50)
    t.setheading(360)
    t.forward(100)

def rhombus():
    t = turtle.Turtle()
    t.color("blue")
    t.goto(0,-1)
    t.goto(200,-1)
    t.color("black")
    t.setheading(40)
    t.forward(70)
    t.setheading(180)
    t.forward(70)
    t.setheading(220)
    t.forward(70)
    t.setheading(360)
    t.forward(70)

def parallelogram():
    t = turtle.Turtle()
    t.color("blue")
    t.goto(0,-4)
    t.goto(200,-4)
    t.goto(200,-5)
    t.goto(200,-200)
    t.color("black")
    t.setheading(100)
    t.forward(70)
    t.setheading(170)
    t.forward(70)
    t.setheading(280)
    t.forward(70)
    t.setheading(350)
    t.forward(70)


draw()