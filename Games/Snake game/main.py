'''Importing all the classes required.'''
from turtle import Screen, distance
from snake import Snake
from food import Food
from scores import Score
import time

screen = Screen() # importing class Screen()
screen.setup( width = 600, height= 600) # Setting up the dimensions of the screen to 600*600 
screen.bgcolor("black") # Setting the background color to black
screen.title("Snake game") 
screen.tracer(0)

snake = Snake() # Creating the snake object from Snake class
food = Food() # Creating the food object from Food class
scores = Score() # Creating score object to keep in check the score

screen.listen() #It enables to listen to the onclick method.
'''Using the arrow keys for the movement of the snake'''
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)

    snake.move() # Moving the snake
    
    # Detect the collision with the food
    '''After the collision with the food :
    1) The snake eats the food (i.e the food will move to a new random location)
    2) The length of the snake increases(i.e a segment is added to the snake_body)
    3) The score is updated by 1. '''
    
    if snake.snake_head.distance(food) < 15 :
        food.new_place() # Moving the food to a new random position
        snake.extend_snake() #Extending the lenggth of the snake
        scores.increase_score() #Updating the score by 1
    
    # Detect the collision with the wall
    '''After the collision with the wall, game is over'''
    
    if snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295 :
        scores.reset()
        snake.reset()

    # Detect the collision with the tail of the snake
    '''After the collision with the tail of the snake(i.e any segment of the snake_body), game is over'''

    for segment in snake.snake_body : #Looping through the segments in the snake_body
       
        if segment == snake.snake_head:
            pass # Case to avoid calling game_over right at the beginning of the game(i.e when the distance between segments is already less than 10 )
        
        elif snake.snake_head.distance(segment) < 10 :
            scores.reset()
            snake.reset()


screen.exitonclick() #Exiting the screen only when the mouse is clicked on the screen. 