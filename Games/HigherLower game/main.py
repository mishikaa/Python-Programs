from art import logo
print(logo)

import random 

from data import data

print("Compare A: ")
opt_1 = random.choice(data.name)
print(opt_1)

from art import vs
print(vs)

print("Against B: ")
opt_2 = random.choice(data.name)
print(opt_2)

choice = input("Which has more followers ? Type 'A' or 'B' : ").lower()


