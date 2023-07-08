from turtle import Turtle, Screen # Importing Turtle & Screen classes from turtle module
import random # Importing random module

players_color = ["violet","indigo","blue","green","yellow","orange","red"] #Setting the colors of the turtles as VIBGYOR
all_players = [] # Creating an empty list to store the various players(as objects)

def is_valid(user_color) :
    '''Function to find whether the user input color is one of the VIBGYOR colors or not'''
    
    for item in players_color :
        if user_color == item :
            check = 1
            break  
        else :
            check = 0   
    
    return check


screen = Screen() # Declaration of a screen object from Screen class
screen.setup(width = 500,height = 500) #Setting the width & the height of the main window

user_bet = screen.textinput(title="Make your bet",prompt = "Which turtle will win the race? Enter a color(From VIBGYOR): ").lower() #Displaying a prompt message on the screen

#Case if the user has entered the wrong input
while is_valid(user_bet) == 0 :
    user_bet = screen.textinput(title="Correct your bet",prompt = "You've entered an invalid color. Enter from VIBGYOR: ").lower() 
    

y_coordinate = -100 # Setting the initial y-coordinate of the turtle

for player_index in range(7) :
    player = Turtle(shape="turtle") #Setting each player's(object) shape as "turtle"
    player.penup() # Moving the pen up
    player.color(players_color[player_index]) # Setting different colors to each player object
    
    player.goto(x = -240, y = y_coordinate) #Keeping the x-coordinate fixed, & shifting the y-coordinate for each player by 50
    y_coordinate += 50
    
    all_players.append(player) # Appending each player object in the list

race_start = False 

if user_bet :
    race_start = True 

while race_start :
    for player in all_players:
        if player.xcor() > 230: #The race will be comppleted if the x-coordinate of the player becomes greater than 230
            winner = player.pencolor() #Storing the winner color 
            race_start = False #This shows that the race has been finished
            break #Coming out of the for loop as soon as we get the winner
            
        player.forward(random.randint(1,20)) #Moving each player forward randomly between the range 1-20

if winner == user_bet :
    print(f"Bravo! You bet on the winning turtle!\nThe {winner} turtle is the winner.")
else :
    print(f"Oops! You lost the bet!\nThe {winner} turtle is the winner.") 

screen.exitonclick()