import turtle
from turtle import*

class myTurtle():
    def __init__(self, shape):
        self.turtle = Turtle()
        self.turtle.shape(shape)

    def move(self) :
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(30)
        self.turtle.left(90)
        self.turtle.forward(100)

    def left(self, angle) :
        self.turtle.left(angle)

t1 = myTurtle("circle")
t2 = myTurtle("turtle")

t1.left(180)
t1.move()
t2.move()

turtle.done()
