import turtle

class quadrilateral:
    #Code
    def _init_(self,name):
        self.name=name

    def parent(self):
         for base in self.__class__.__bases__:
             print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(-280, 20)
        t.pendown()
        t.goto(-265, 120)
        t.goto(-185, 105)
        t.goto(-170, 35)
        t.goto(-280, 20)

class kite(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(-250, 200)
        t.pendown()
        t.goto(-200, 270)
        t.goto(-150, 200)
        t.goto(-200, 160)
        t.goto(-250, 200)

class trapezoid(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(-320, -130)
        t.pendown()
        t.goto(-305, -50)
        t.goto(-225, -50)
        t.goto(-180, -130)
        t.goto(-320, -130)

class parallelogram(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.color("white")
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

class isosceles(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(140, 120)
        t.pendown()
        t.goto(175, 200)
        t.goto(245, 200)
        t.goto(280, 120)
        t.goto(140, 120)

class rectangle(parallelogram,isosceles):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.color("white")
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

class rhombus(kite,parallelogram):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.color("white")
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

class square(rhombus,rectangle):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)
    def show(self):
        t = turtle.Turtle()
        t.setheading(90)
        t.forward(100)
        t.setheading(180)
        t.forward(100)
        t.setheading(270)
        t.forward(100)
        t.setheading(360)
        t.forward(100)

window = turtle.Screen()

print("\nquadrilateral\nparents:")
Quad_foo = quadrilateral()
Quad_foo.parent()
Quad_foo.show()

print("\nkite\nparents:")
kite_foo = kite()
kite_foo.parent()
kite_foo.show()

print("\ntrapezoid\nparents:")
trapezoid_foo = trapezoid()
trapezoid_foo.parent()
trapezoid_foo.show()

print("\nparallelogram\nparents:")
parallelogram_foo = parallelogram()
parallelogram_foo.parent()
parallelogram_foo.show()

print("\nisosceles\nparents:")
isosceles_foo = isosceles()
isosceles_foo.parent()
isosceles_foo.show()

print("\nrectangle\nparents:")
rectangle_foo = rectangle()
rectangle_foo.parent()
rectangle_foo.show()

print("\nrhombus\nparents:")
rhombus_foo = rhombus()
rhombus_foo.parent()
rhombus_foo.show()

print("\nsquare\nparents:")
square_foo = square()
square_foo.parent()
square_foo.show()
window.exitonclick()