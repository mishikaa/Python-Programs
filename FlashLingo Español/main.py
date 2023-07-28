from tkinter import *
import pandas
import random
import math

background_color = '#f3fae1'

current_card = {}
to_learn = {}
timer = 4

# Reading data from words_list.csv file
try: 
    data = pandas.read_csv("./data/words_to_learn.csv")
    
except FileNotFoundError:
    original_data = pandas.read_csv('./data/words_list.csv')
    to_learn = original_data.to_dict(orient="records")

else:        
    # Converting the csv data into dictionary with the column name as key and each row data as value for each entry
    to_learn = data.to_dict(orient="records")


def generate_next_card(): 
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn) # Gives a random entry from to_learn 
    reset_timer()

    canvas.itemconfig(card_background, image=front_card)
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_card["spanish"], fill="black")
    flip_timer = window.after(4000, func=card_flip)


def reset_timer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="4:00")
    countdown(4)


'''COUNTDOWN MECHANISM'''
def countdown(count):
    # Converting the time in minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # To display double digits in seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    # Changing the text of the timer 
    timer_label.config(text=f"{count_min}:{count_sec}")
    
    # After each second, calling the function recursively with decremented value of count 
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)


# If user clicks on known button, then remove it from csv
def is_known():
    to_learn.remove(current_card)
    
    # Creating a new csv file for the words not known to user
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)


    generate_next_card()

def card_flip():
    # Changing the words
    canvas.itemconfig(title, text="English", fill="#fff")
    canvas.itemconfig(word, text=current_card["english"], fill="#fff")

    # Changing the canvas image
    canvas.itemconfig(card_background, image=back_card)


''' UI Setup'''
# Screen setup
window = Tk()
window.title("FlashLingo Español")
window.config(padx = 50, pady=50, bg=background_color)

flip_timer = window.after(5000, func=card_flip)

# Image of the cards
front_card = PhotoImage(file='./images/front.png')
back_card = PhotoImage(file='./images/back.png')

# Storing the card's width and height
card_width = front_card.width()
card_height = front_card.height()

# Creating the canvas of cards' size
canvas = Canvas(width=card_width, height=card_height)

card_background = canvas.create_image(card_width / 2, card_height / 2, image=front_card)

canvas.config(bg=background_color)
# Placing the canvas on the screen
canvas.grid(row=0, column=0, columnspan=3)

# Adding texts on the canvas
title = canvas.create_text(card_width/2, card_height/2-50, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(card_width/2, card_height/2+50, text="Word", font=("Ariel", 42, "bold"))

# Creating the buttons
unknown_icon = PhotoImage(file='./images/unknown.png')
unknown_btn = Button(image=unknown_icon, highlightthickness=0, command=generate_next_card)
unknown_btn.grid(row=1, column=0)

timer_label = Label(text="4:00", font=("Ariel", 32, "bold"), bg=background_color, fg="#2b2d42")
timer_label.grid(row=1,column=1)

known_icon = PhotoImage(file='./images/known.png')
known_btn = Button(image=known_icon, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=2)

# Calling for the 1st time to generate a flashcard
generate_next_card()

window.mainloop()