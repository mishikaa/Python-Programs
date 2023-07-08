from turtle import Turtle
import random

INCREASING_FACTOR = 10
BARRIER_COLOR = ["deep sky blue","aquamarine","dark goldenrod","light pink","pale violet red","medium purple","navy","light salmon","steel blue","green","blue","orange","lawn green","red","lime","gold","medium spring green","green yellow","pale green","orange red","firebrick","forest green"] #List of colors to select a random color for each barrier

class Barriers :
   
    def __init__(self) :
        self.all_barriers = []
        self.barrier_speed = INCREASING_FACTOR
    
    def create_barriers(self) :
        
        chance_to_create_barrier = random.randint(1,5) #To create a limited amount of bricks so that the player can cross them
        
        if chance_to_create_barrier == 1:
            
            #Creating the barriers
            new_barrier = Turtle("square")
            new_barrier.shapesize(stretch_wid=1, stretch_len=2)
            new_barrier.penup()
            new_barrier.color(random.choice(BARRIER_COLOR))
           
            random_y = random.randint(-250,250)
            new_barrier.goto(300, random_y)
            self.all_barriers.append(new_barrier)

    def move(self) :
        '''Function to move each and every barriers'''
        
        for barrier in self.all_barriers :
            barrier.backward(self.barrier_speed) #Moving the barriers in backward direction so that it could hit the player

    def level_speed(self) :
        '''Function to increase the speed when level is increased'''
        self.barrier_speed += INCREASING_FACTOR

