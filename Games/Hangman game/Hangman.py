import random #importing the random module for selecting a random word from the list of words

print("#################### Welcome to #######################")
from game_art import hangman_word #importing the ascii art of the word-hangman
print(hangman_word)
print("#######################################################\n")

# Asking the player for choosing the difficulty level of game
level = int(input("########Select the difficulty  level :########\nEnter 1 for Easy, 2 for Medium and 3 for Hard: \n")) 

# Asking the player to input an option again out of the given choices if they have inputted any other number other than the given choices
while (level != 1 and level != 2 and level != 3) :
    print("Invalid choice.Enter again")
    level = int(input("########Select the difficulty  level :########\nEnter 1 for Easy, 2 for Medium and 3 for Hard:\n"))

from hangman_words import words_list
chosen_word = random.choice(words_list[level-1])

display = [] #Declaring an empty list
#Storing _ in each list item
for size in range(len(chosen_word)):
  display.append('_') 

print(' '.join(display)) #Printing the blanks

print(f"Now start guessing the letters\n")
user_choice = [] #Declaring an empty list to store all the guesses made by the player
lives = 6 #Man will die if total of 6 wrong choices are made
game_end = False #To check whether game is over or not

while not game_end :

    guess = input("Guess a letter: ").lower() #Asking the player to make a guess

    if guess in user_choice: #Condition if that guess has been made earlier
        print(f"You've already guessed {guess}")

    elif guess not in chosen_word: #Condition if the guess is wrong
        print(f"Oops!Letter {guess} is not in the word. You lost a life")
        lives -= 1 #Reducing the life of the hanging man
    
    else: #Condition if the guess is correct i.e. if the random word contains the guessed letter
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
               display[index] = guess
 

    print(' '.join(display)) 

#Importing the ascii art of hanging man as per the lives
    from game_art import game_pic
    if '_' not in display :
        print("Bravo! You win!")
        game_end = True
        print(game_pic[7])
    elif(lives == 0) :
        print("You lose.")
        game_end = True
        print(game_pic[0])
    else:   
        print(game_pic[lives])
        user_choice.append(guess)

print(f"The correct word is : {chosen_word}")
