from turtle import Turtle

START = (0,-280)
DISTANCE_MOVED = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        #Setting up the player
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90) #Pointing it in north direction

    def move_forward(self) :
        '''Function to move the player forward'''
        
        self.forward(DISTANCE_MOVED)
    
    def go_to_start(self) :
        '''Function to bring the player back at its starting point'''
        
        self.goto(START)

    def is_at_finish(self) :
        '''Function to check if the player has reached the finish line.'''
        
        if self.ycor() > FINISH_LINE :
            return True
        else:
            return False

        
