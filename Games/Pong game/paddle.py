from turtle import Turtle
import random

paddle_color = ("green","orange","lawn green","red","lime","gold","medium spring green","green yellow","pale green","orange red","yellow","firebrick","forest green")
class Paddle(Turtle): #Creating a Paddle class which inherits the Turtle class

    def __init__(self,pos) :
        super().__init__() #Inheriting the Turtle class in Paddle class
        
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color(random.choice(paddle_color)) # Randomly choosing the color for the paddles from the tuple paddle_color    
        self.penup() # Moving the pen up so that it doesn't draw a line
        self.goto(pos) # Moving it to a specified position

    def go_up(self) :
        ''' Function to move the paddle upwards by 30 paces from its previous y_coordinate'''
        new_y = self.ycor() + 30
        
        '''Condition that the paddle does not move beyond y = 280 units.'''
        if new_y >= 280 :
            new_y = self.ycor() - 30
        
        self.goto(self.xcor(),new_y)
    
    def go_down(self) :
        ''' Function to move the paddle downwards by 30 paces from its previous y_coordinate'''      
        new_y = self.ycor() - 30
        
        '''Condition that the paddle does not move beyond y = -280 units.'''
        if self.ycor() <= -280 :
            new_y = self.ycor() + 30
        
        self.goto(self.xcor(),new_y)
