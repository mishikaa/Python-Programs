from turtle import Turtle
import random

class Food(Turtle): # Inheriting the super class 'Turtle'
    
    def __init__(self) :
        super().__init__()
        
        self.shape("square") #Creating the food of square shape
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5) #Setting the shape size to a specified size
        self.color("yellow")
        self.speed("fastest")
        
        self.new_place() #Calling new_place() to move the food to a new position

    def new_place(self) :   

        # Generating a random location for the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y) #Moving the food to the random position

    