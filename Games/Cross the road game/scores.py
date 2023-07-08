from turtle import Turtle

class Scores(Turtle) :
    def __init__(self) :
        super().__init__()
      
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()

    def update_score(self) :
        self.write(f"Level: {self.level}", align="left", font = ("Courier",20,"normal"))

    def game_over(self) :
        self.goto(0,0)
        self.write("Game over!",align ="center",font = ("Courier",30,"normal"))
        
   
    def level_up(self) :
        self.level += 1
        self.clear()
        self.update_score()