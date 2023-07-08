import pandas
import turtle

screen = turtle.Screen()
screen.setup( width = 750, height= 800) # Setting up the dimensions of the screen to 600*600 
screen.title("States Stomp")
screen.bgcolor("#e2eafc")

image = "india_blank_map.gif" # Storing the image name in a variable
screen.addshape(image) # Adding the image as shape to the screen

# Adding shape to screen 
turtle.shape(image) # Setting the turtle's shape as the image

game_on = True

# Fetching the data from the csv file
data = pandas.read_csv('./states_data.csv')
states = data.state.to_list() # Converting the state column to a list
# print(states)

guessed_states = []
while len(guessed_states) < len(states):
    # Input popup box
    answer = screen.textinput(title=f"{len(guessed_states)}/28 states correct", prompt="What's another state's name?").title()
    # Exit the game
    if answer == "Exit":
        break
    
    # If the inputted state is correct
    if (answer in states):
        guessed_states.append(answer)
        states.remove(answer) # Removing the correct guessed state name from states list so that at the end, it contains the names which have not been guessed
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        x_coor = (state_data.x.iloc[0])
        y_coor = (state_data.y.iloc[0])
        t.goto(x_coor, y_coor)
        t.write(answer)
    
    
# Once the game is over or exitted, storing the states that have not been guessed into a csv file:
states_not_guessed = {
    "state": states
}
df = pandas.DataFrame(states_not_guessed)
df.to_csv("./states_to_learn.csv")