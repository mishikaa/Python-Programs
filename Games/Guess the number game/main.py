import random
from art import logo #Importing the logo from art.py

def game(lives) :
    '''Function to make thee guesses.
    If the guess is right and you've lives remaining, then you win
    or else lose the game'''

    print(f"You have {lives} lives to guess the number.")
    
    if lives > 0 : #case when lives are remaining

        while(lives > 0) :
            guess_no = int(input("Guess a number : "))

            if correct_no == guess_no :
                print(f"\nBravo!🥳 You got it right! The number was {correct_no}.\n")
                break # Terminating the game when the player guessed the number right
            
            elif guess_no > correct_no :
                print("Too high.")
                lives -= 1 #Reducing the number of times the player can guess.
                print(f"You have {lives} lives remaining to guess the correct number.")

            else :
                print("Too low.")
                lives -= 1
                print(f"You have {lives} lives remaining to guess the correct number.")
    
    else : #Case when the player runs out of guesses.

        print(f"You have run out of guesses.")
        print(f"\nOops! You couldn't guess the number correctly.😕 The correct number was {correct_no}.\n")
    

print("\t\t########### Welcome to GUESS THE NUMBER game !###########\n")

print("I'm considering a number between 1 and 100. Can you figure out what it is?")
correct_no = random.randint(1,100) #Choosing a random no. between 1 to 100

level = input("\nSelect the difficulty level : Type 'e' for EASY ,'m' for MEDIUM, and 'h' for HARD LEVEL : ").lower()
print()

#Asking the player to input again when he/she has entered something else other than 'e','m' or 'h'

while (level != 'e' and level != 'm' and level != 'h') :
    print("Invalid input.")
    level = input("Type 'e' for EASY ,'m' for MEDIUM, and 'h' for HARD LEVEL : ").lower()
    print() 

#Storing the lives according to the difficulty level choosen by the player.    
if level == 'e' :
    lives = 12
elif level == 'm' :
    lives = 8
else :
    lives = 5

game(lives) #calling the function game() with lives as parameter




        




