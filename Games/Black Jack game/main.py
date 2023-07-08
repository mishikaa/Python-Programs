import random 

#For clearing the console screen after each round
from os import system, name 
def clear(): 
    _ = system('cls')  

from art import logo, playing_cards #Importing logo of blackjack and playing cards from art.py

def win_lose(user_score,dealer_score) :
    '''Function to find the result of the game'''
    if(user_score > dealer_score and user_score <= 21) : #User wins if his/her score is greater than the dealer & less than 22
        return "You win! 😎"
    elif (dealer_score > 21 and user_score <= 21) : # User can also win if dealer score is greater than 21 & user's score is less than 22
        return "Opponent went over! You win! 😁"
    elif (user_score > 21) : # User will lose if his/her score exceeds 21
        return "You went over ! You lose 😪"
    elif (user_score < dealer_score) : # User loses if his/her score is less than the dealer's score
        return "You lose 🥺"
    
    else :
        return "It's a draw🤝" #There'll be a draw if both the scores are equal

# Ace can have value 1 or 11 depending on the score.
# If the score is exceeding 21 , then ace takes the value as 1 otherwise its value is 11.
def ace_check(card_list) :
    for index in range(len(card_list)) :
        if card_list[index] == 11 and sum(card_list) > 21:
            card_list[index] = 1

# Function to print the cards
def print_cards(cards):
    for card in list(cards):
        print(playing_cards[card])

def game() :
    '''Function for the blackjack game''' 

    print("\n\t\t######## WELCOME TO #########")
    print(logo)

    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] # Storing the card values in a list

    user_cards = [] # Creating an empty list to store the user's cards
    dealer_cards = [] # Creating an empty list to store the dealer's cards
    
    # Providing Initial cards to both dealer and the user
    for add_card in range(2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    
    print(f"Your cards are {user_cards}")
    print("Your current score is :",sum(user_cards))

    print(f"\nDealer's 1st card is {dealer_cards[0]}")

    choice = 'h'
    while choice == 'h' or choice == 's':
        choice = input("\nDo you want to HIT or STAND ? Enter 'h' to HIT and 's' to STAND : ").lower()
        
        while(choice != 'h' and choice != 's') : #Case if the user types a wrong input 
            print("Invalid Input!")
            choice = input("Enter 'h' to HIT and 's' to STAND : ").lower()
    
        if choice == 'h' and sum(user_cards) <= 21 : #When the user chooses to HIT & his/her sum<=21
        
            user_cards.append(random.choice(cards)) #If user selects hit, then adding more cards 
        
            #if anyone is having the ace card
            if(11 in user_cards and sum(user_cards) > 21) : #If ace is present in user's cards & checking whether the sum is > or <= 21
                ace_check(user_cards) #calling the function ace_check()

                print(f"\nYour cards are {user_cards}")
                print("Your current score is :",sum(user_cards))

                print(f"\nDealer's 1st card is {dealer_cards[0]}")

            elif(11 in dealer_cards and sum(dealer_cards) > 21) : #If ace is present in dealer's cards & checking whether the sum is > or <= 21
                ace_check(dealer_cards)

                print(f"\nDealer's 1st card is {dealer_cards[0]}")
            
            #if none of them is having the ace card
            else :
                print(f"\nYour cards are {user_cards}")

                print("Your current score is :",sum(user_cards))

                print(f"\nDealer's 1st card is {dealer_cards[0]}")

            
        if (choice == 'h' and sum(user_cards) > 21) or choice == 's' : #Case When the user chooses to STAND or his/her sum exceeds 21
                       
            user_total = sum(user_cards) #Storing the sum of user's cards
            dealer_total = sum(dealer_cards) #Storing the sum of Dealer's cards
        
            while( dealer_total < 17 ) : #There is a rule that the dealer will keep drawing cards till he/she has the sum greater than or equal to 17
                dealer_cards.append(random.choice(cards))
                dealer_total = sum(dealer_cards)
        
            print(f"\nYour final hand is : {user_cards}")
            print_cards(user_cards)

            print(f"Your final score : {user_total}")
            print(f"\nDealer's final hand is : {dealer_cards}")
            print_cards(dealer_cards)

            print(f"Dealer's final score : {dealer_total}")
        
            result = win_lose(user_total,dealer_total)
            print("\n########## ",result," ##########\n")
            break #Terminating from the while loop after displaying the result
#end of game()


play_yes_no = 'y'

while(play_yes_no == 'y') :
    game() 
    play_yes_no = input("Do you want to continue playing BLACKJACK? Enter 'y' for YES and 'n' for NO : ").lower()
    clear()
    
    while(play_yes_no != 'y' and play_yes_no!= 'n') : #Asking the user to input the correct value
        print("Invalid Input!")
        play_yes_no = input("Enter 'y' for YES to continue and 'n' for NO to exit : ").lower()
        clear()
    

print("\n\t\t########## Thankyou for playing!🤗 ##########\n\n")