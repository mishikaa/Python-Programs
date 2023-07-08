'''Importing the required classes'''
from turtle import Screen
from player import Player
from barriers import Barriers
from scores import Scores
import time

'''Setting up the screen'''
screen = Screen()
screen.setup( width = 600, height = 600 )
screen.tracer(0)
screen.title("Cross the road game")

'''Initialising the objects of different classes'''
player = Player()
barriers = Barriers()
scores = Scores()

'''Setting up the key'''
screen.listen()
screen.onkey(player.move_forward,"Up")

game_on= True

while game_on :
    time.sleep(0.1)
    screen.update()
   
    barriers.create_barriers() # Creating the barriers
    barriers.move() #Calling the function to move the barriers

    '''Detecting collision with the barrier'''
    for barrier in barriers.all_barriers :
        if player.distance(barrier) < 20:
            game_on = False #Game stops
            scores.game_over() #Calling function to print 'Game over'

    '''Case if the player succeeds in reaching the finish line'''
    if player.is_at_finish() :
        
        player.go_to_start() #Moving the player back to its original position from where it started
        scores.level_up() #Leveling up
        barriers.level_speed() #Increasing the speed after the level is increased
    
screen.exitonclick()