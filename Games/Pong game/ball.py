from turtle import Turtle

FONT_STYLE = ("Times New Roman", 50, "Normal") #Storing the font styles in a tuple

class Ball(Turtle) :
    def __init__(self) :
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()

        self.speed_increase = 0.09
        self.x_move = 10
        self.y_move = 10
        '''Note: Original position of ball is (0,0).'''
    
    def move_ball(self):
        '''Function to move the ball.'''
       
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        
        self.goto(new_x, new_y)
    
    def bounce_ball_in_y(self) :
        '''Function the make the ball bounce in opposite direction when it hits the wall.'''
        
        self.y_move *= -1

    def bounce_ball_in_x(self) :
        '''Function the make the ball bounce in opposite direction when it hits any padddle.'''
       
        self.x_move *= -1
        self.speed_increase *= 0.9  #Increasing the speed of the ball whenever it hits the ball.      

    def reset_ball(self) :
        '''Function to reset the ball back to (0,0)'''
        
        self.goto(0, 0) # Setting the ball to center.
        self.speed_increase = 0.09 # Resetting the speed of the ball.
        self.bounce_ball_in_x()