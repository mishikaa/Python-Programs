from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("PassFort")
window.config(padx=50, pady=50)

def save_data():
    website = website_entry.get()
    email_username = emailUsername_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email_username": email_username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The details entered: \nWebsite: {website}\nEmail: {email_username}\nPassword: {password}\n\nAre you sure you want to save?")
        
        if is_ok:
            try:
                with open("./data.json", mode="r") as file:
                    # Reading old data from the json file
                    data = json.load(file)
                    # print(data)
        
            # If json file does not exist already
            except FileNotFoundError:
                with open('./data.json', mode="w") as file:
                    # Writing a fresh JSON object to it (with our first key-value pair).    
                    json.dump(new_data, file, indent=4)
            else:
                # Updating the old data
                data.update(new_data)
            
                with open("./data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            
            # Runs no matter an exception is thrown or not
            finally:
                # Resetting the input fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)


'''PASSWORD GENERATOR'''
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password) # To copy the password automatically in the clipboard

'''SEARCH THROUGH THE DATA'''
def search():
    website_name = website_entry.get()
    
    try:
        with open('./data.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('./data.json', mode="w") as file:
            messagebox.showinfo(title="Error", message="No data file found.")

    else:         
        # If a website with given name(key) exists
        if website_name in data:
            email_username = data[website_name]["email_username"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email/username: {email_username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not found", message=f"No data for website: {website_name} exists.")

'''UI SETUP'''
# Creation of canvas

canvas = Canvas(width=192, height=192)
# Setting up the image on the canvas
password_img = PhotoImage(file='./password.png')

canvas.create_image(120, 96, image=password_img)
canvas.grid(row=0, column=1)

# Website Input Section
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1)

# Search button
search_btn = Button(text="Search", width=14, command=search)
search_btn.grid(row=1,column=2)

# Email Input Section
emailUsername_label = Label(text="Email/username:")
emailUsername_label.grid(row=2, column=0)

emailUsername_entry = Entry(width=50)
emailUsername_entry.insert(0, "alex@gmail.com")
emailUsername_entry.grid(row=2, column=1, columnspan=2)

# Password Input Section
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, columnspan=1)

# Generate password button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

# Add Button
add_btn = Button(text="Add", width=44, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)
    

window.mainloop()