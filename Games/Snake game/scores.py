from turtle import Turtle # Importing Turtle class from turtle module

FONT_STYLE = ("Courier", 20, "bold") # Storing the font styles in a tuple

class Score(Turtle) : # Creating an inherited class Score
    
    def __init__(self) :
        super().__init__()
       
        self.score = 0
        
        with open("./Snake game/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        
        self.color("white")
        self.hideturtle() # Hiding the turtle so that it is not visible on the screen
        self.penup()
        self.goto(0,270) # Moving the turtle at the top of the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font = FONT_STYLE)
    
    def increase_score(self):
        self.score += 1
        self.update_score()
   
    def update_score(self) : # Function defined to update the score
       
        self.clear() # Clearing the previous score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font = FONT_STYLE)
    
    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            
            # Writing the high score in the  Snake game/data.txt
            with open("./Snake game/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        
        self.score = 0
        self.update_score()
    
    # def game_over(self) :
       
    #     self.goto(0, 0) # Setting the turtle to center
    #     self.write("GAME OVER!", align="center", font = FONT_STYLE)