from tkinter import *
import math

'''CONSTANTS'''
RED = "#e7305b"
GREEN = "#9bdeac"
GREEN2 = "#4dc126"
YELLOW = "#FFF7D4"
GRAY = "#F9FBE7"
PURPLE="#A076F9"
BLUE="#1B6B93"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


'''FUNCTION DEFINITION'''
def start_timer():
    global repetitions
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # Long break
    if(repetitions % 8 == 0):
        timer_label.config(text="Long break", fg=RED)
        countdown(long_break_sec) 
    
    # Short break
    elif(repetitions % 2 == 0):
        timer_label.config(text="Short break", fg=RED)
        countdown(short_break_sec)
    
    # Work time
    else:
        timer_label.config(text="Work", fg=PURPLE)
        countdown(work_sec)
            
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global repetitions
    repetitions = 0
    check_mark.config(text="")


'''COUNTDOWN MECHANISM'''
def countdown(count):
    # Converting the time in minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # To display double digits in seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    # Changing the text of the timer 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    # After each second, calling the function recursively with decremented value of count 
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sess = math.floor(repetitions/2)
        for _ in range(work_sess):
            marks += "✔"
        check_mark.config(text=marks)


'''UI SETUP'''
window = Tk()
window.title("TomatoTik")
window.config(padx=100, pady=100, bg=YELLOW)

# Setting the Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN, pady=5)
# timer_label.pack(side="top")
timer_label.grid(row=0, column=1)

# Creating the canvas
canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
# Adding the image to the canvas
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(256, 256, image=bg_image)
timer_text = canvas.create_text(256,400, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
# canvas.pack()
canvas.grid(row=1, column=1)

# Creating buttons
start_btn = Button(text="Start", bg="white", activebackground=GRAY, font=(FONT_NAME, 14), width=8, highlightthickness=0, command=start_timer)
# start_btn.pack(side="left")
start_btn.grid(row=2, column=0)


reset_btn = Button(text="Reset", bg="white", activebackground=GRAY, font=(FONT_NAME, 14), width=8, highlightthickness=0, command=reset_timer)
# reset_btn.pack(side="right")
reset_btn.grid(row=2, column=2)

# Checkmark label
check_mark = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN2, background=YELLOW)
# check_mark.pack(side="bottom")
check_mark.grid(row=3, column=1)


window.mainloop()