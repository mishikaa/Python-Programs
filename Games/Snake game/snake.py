from turtle import Turtle
import random

# List of colors to select a random color for each segment of the snake's body
SNAKE_COLOR = ["green","orange","lawn green","red","lime","gold","medium spring green","green yellow","pale green","orange red","firebrick","forest green"] 

# Storing the initial coordinates of the 1st 3 segments of the snake
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)] 

MOVE_DISTANCE = 20 
'''For setting up the directions in which the snake moves '''
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :

    def __init__(self) :
       
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self) :
        '''Creating the snake segment wise'''

        for coordinates in STARTING_POS :
            self.add_segment(coordinates) # Adding the initial 3 segments of the snake body one by one
    
    def add_segment(self,coordinates) : # Adding snake's segment one by one
        
        new_segment = Turtle(shape = "circle") # Setting a new_segment object of 'circular' shape
        new_segment.color(random.choice(SNAKE_COLOR)) # Choosing any random color from the list for each segment
        new_segment.penup() # Moving the pen up so that it do not draw a line while moving 
        new_segment.goto(coordinates) # Adding a new segment at the specified coordinates
        self.snake_body.append(new_segment) # Appending the new segment to the snake's body

    def extend_snake(self) :
        #  Increase the length of snake via adding a new segment in snake body
        self.add_segment(self.snake_body[-1].position()) # Calling add_segment()for adding a segment to snake's body at the tail(i.e at the last segments's position)

    def up(self) :
        '''Moving the snake upwards only when the snake is not moving in downward direction'''
        
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90) # Setting the head of the snake_head to 90 degrees
    
    def down(self) :
        '''Moving the snake downwards only when the snake is not moving in upward direction'''
        
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270) # Setting the head of the snake_head to 270 degrees

    def left(self) :
        '''Moving the snake left only when the snake is not moving in right direction'''
       
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180) # Setting the head of the snake_head to 180 degrees

    def right(self) :
        '''Moving the snake right only when the snake is not moving in left direction'''
        
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0) # Setting the head of the snake_head to 0 degree

    def move(self) :
        
        for seg_no in range(len(self.snake_body) - 1, 0, -1):      
             new_x = self.snake_body[seg_no - 1].xcor()
             new_y = self.snake_body[seg_no - 1].ycor()
             self.snake_body[seg_no].goto(new_x, new_y)
        
        self.snake_head.forward(MOVE_DISTANCE) # Moving the snake forward by 20 steps each time

    def reset(self):
        # Moving the previous snake out of the screen
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        
        # Creating a new snake and centering it 
        self.create_snake()
        self.snake_head = self.snake_body[0]
