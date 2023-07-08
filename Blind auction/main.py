# To clear the console screen so that the next bidder cannot see the previous bidding amount
from os import system, name 
def clear(): 
    _ = system('cls') 

auction_details = {} #Creating an empty dictionary to store the Bidder's name & the bidding amount respectively

print("\n\t\t###### Welcome to the BLIND AUCTION PROGRAM ######\n")

more_bidders = 'y' #Variable to store whether more bidders are there or not

while more_bidders == 'y':

    name = input("What's your name ? ").title()
    ans = name != '' and all(chr.isalpha() or chr.isspace() for chr in name) #To check if the bidder has not entered anything except alphabets or space in their names
    
    #Asking the bidder to enter the name repeatedly till he/she enters it correctly
    while(ans == False) :
        print("Invalid name. Name should not contain any digits or special characters.")
        name = input("Enter your name again : ").title()
        ans = name != '' and all(chr.isalpha() or chr.isspace() for chr in name)
    
    bid = input("What's your bidding ? $")
    bid_check = bid.isdigit() #To check if the bidding amount contains only positive integers

    if bid_check == True :
        bid = int(bid)

    #if the bidder has entered a negative or a anything except the digits ,it'll ask him/her to enter it correctly
    else :
        while bid_check == False :
            print("Invalid format of the bidding amount.\nNote : It cannot contain anything except digits. ")
            print("\tIt should also not contain decimal amount.")

            bid = input("Enter your bid amount again . $")
            bid_check = bid.isdigit()
            if bid_check == True :
               bid = int(bid)


    auction_details[name] = bid #Storing the bid values with their names as the key

    more_bidders = input("Are there any more bidders? Type 'Y' for YES and 'N' for NO : ").lower()
    
    #Case if there are more bidders
    if (more_bidders == 'y') :
        clear()

    #case if the bidder has entered any other alphabet other than y or n
    elif more_bidders != 'y' or more_bidders != 'n' :
        while more_bidders != 'y' and more_bidders != 'n' :
            print("\nInvalid choice. Please enter again.")
            more_bidders = input("\nType 'Y' for YES and 'N' for NO : ").lower()
            if (more_bidders == 'y') :
               clear()

#Finding the highest bidder in the blind auction
highest_bid = -999

for bidder in auction_details :

    if(auction_details[bidder] > highest_bid) :
        highest_bid = auction_details[bidder]
        highest_bidder = bidder

print(f"\nThe winner is {highest_bidder} with the highest bid of ${highest_bid}!\n\t\tCongratulations!")
