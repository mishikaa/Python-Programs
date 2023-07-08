#  Importing the required classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen() # importing class Screen()
screen.setup( width = 800, height= 600) # Setting up the dimensions of the screen to 800*600 
screen.bgcolor("black") # Setting the background color to black
screen.title("Ping & Pong game") #  Setting up the title 

screen.tracer(0) # Turning off the animation

'''Creating 2 objects from class Paddle'''
r_paddle = Paddle((370,0)) #  Right paddle is at the coordinates (370,0) .
l_paddle = Paddle((-370,0)) #  Left paddle is at the coordinates (-370,0) .

'''Creating an object named 'ball' from Ball class'''
ball = Ball()

'''Creating an object named 'score' from Score class'''
score = Score()

'''Setting up the control keys of both the paddles.'''
screen.listen()
#  For right paddle:
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#  For left paddle:
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on :
    
    time.sleep(ball.speed_increase)
    screen.update()
    
    ball.move_ball() #  Calling the function move_ball() to move the ball
    
    #  Detecting collision with the wall 
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        
        ball.bounce_ball_in_y() #  Calling the function bounce_ball_in_y() to bounce the ball in opposite direction when it hits the wall.

    #  Detecting collision with the paddle
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 340) or (ball.distance(l_paddle) < 60 and ball.xcor() < -340):
        
        ball.bounce_ball_in_x() #  Calling the function bounce_ball_in_y() to bounce the ball in opposite direction when it hits the paddle.

    #  Case when right paddle misses the ball
    if ball.xcor() > 400 :
        
        ball.reset_ball() # Calling the function to set the ball back to (0,0).
        score.l_gain_point() # Calling the function to increase the score of left paddle by 1.
        
    #  Case when left paddle misses the ball
    if ball.xcor() < -400 :
        
        ball.reset_ball()
        score.r_gain_point() # Calling the function to increase the score of right paddle by 1.

    #  Game is over when someone scores 21 
    if score.l_score == 21 or score.r_score == 21 :
        
        game_on = False
        score.game_over()

screen.exitonclick() # Exiting the screen only when the mouse is clicked on the screen. 