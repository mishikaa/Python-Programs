from asyncore import write
from turtle import Turtle #Importing Turtle class from turtle module

FONT_STYLE = ("Times New Roman", 40, "bold") #Storing the font styles in a tuple

class Score(Turtle) :
    
    def __init__(self) :
        super().__init__()
       
        self.color("white")
        self.hideturtle() #Hiding the turtle so that it is not visible on the screen
        self.penup()
        #Initialising the scores of both the paddles to 0
        self.l_score = 0 
        self.r_score = 0

        self.update_score()
    
    def update_score(self) : #Function defined to update the score
        
        '''Setting the score of the right paddle'''
        self.goto(-150, 190) #Moving the score of the right paddle at the top of the screen
        self.write(self.l_score, align="center", font = FONT_STYLE)
        
        '''Setting the score of the left paddle'''
        self.goto(150, 190) #Moving the turtle at the top of the screen
        self.write(self.r_score, align="center", font = FONT_STYLE)
        
    def l_gain_point(self) :
        
        self.l_score += 1
        self.clear() #Clearing the previous score
        self.update_score()
 
    def r_gain_point(self) :
        self.r_score += 1
        self.clear()
        self.update_score()
    
    def game_over(self) :
        if self.l_score == 21:
            self.winner = "left paddle"
        elif self.r_score == 21 :
            self.winner = "right paddle"
        else :
            self.winner = "both paddles"

        self.goto(0,-10)
        self.write(f"The {self.winner} \n wins the game!", align="center", font = FONT_STYLE)
        
   