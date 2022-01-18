from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(position)
        self.shape("square")
        self.turtlesize(1,5)
        self.right(90)

    def move_down(self):
        self.forward(20)

    def move_up(self):
        self.backward(20)