from all_info import data,resource #importing the menu and the resources from all_info.py

def maker(choice) :
    '''Function to make the beverage if the resources & the money are sufficient'''

    if choice == "latte" or choice == "espresso" or choice == "green tea latte":
        print(f"Price of {choice} is : ₹", data[choice]["price"])

        is_sufficient = is_resource_sufficient(choice) #Checking if the resources are sufficient to make the required beverage
        
        if(is_sufficient == True) :
            change = price(data[choice]["price"])
            
            if(change) >= 0 :
                #Subtracting the quantity resources which have been used to make the beverage
                for item in data[choice]["ingredients"]:
                    resource[item] -= data[choice]["ingredients"][item]
                
                resource["money"] += data[choice]["price"] #Adding the money in the amount in the beverage maker
    
    elif choice == "report":
        report(choice) #Calling the report function to print the report of the maker

def is_resource_sufficient(choice):
    '''Function to check if the resources are sufficient or not to prepare the required beverage'''
    
    for item in data[choice]["ingredients"] :
        if(data[choice]["ingredients"][item] > resource[item]):
            print(f"{item} is not sufficient.")
            return False
            
    return True  

def price(price) :
    '''Function to ask the user to give the required amount and returning the change '''
    
    print("\nEnter money : ")
    rupee_10 = int(input("How many ₹10 notes ? "))
    rupee_20 = int(input("How many ₹20 notes ? "))
    rupee_50 = int(input("How many ₹50 notes ? "))
    rupee_100 = int(input("How many ₹100 notes ? "))
    rupee_200 = int(input("How many ₹200 notes ? "))
    rupee_500 = int(input("How many ₹500 notes ? "))
    
    #Calculating the change 
    change = (rupee_10*10 + rupee_20*20 + rupee_50*50 + rupee_100*100 + rupee_200*200 + rupee_500*500 ) - price

    if change < 0 :
        print("Sorry that's not enough money. Money refunded.")
        return -1
    
    elif change == 0 :
        print(f"\nHere is your {choice}☕. Enjoy!")
        return change   
    
    else:
        print(f"\nHere is ₹{change} in change.")
        print(f"Here is your {choice}☕. Enjoy!")
        return change
        

def report(choice) :
    '''Function printing the report of the beverage maker'''

    print("Water :", resource["water"],"ml")
    print("Milk :", resource["milk"],"ml")
    print("Coffee :", resource["coffee"],"g")
    print("Matcha :", resource["matcha"],"tsp")
    print("Vanilla Syrup:", resource["vanilla syrup"],"tsp")
    print("Money: ₹", resource["money"])

choice = "on"
while(choice != "off") :
    # Inputting the user's choice
    choice = input("\nWhat would you like to have? (Latte/Espresso/Green Tea Latte) \nEnter \"report\" to display the report of the maker \nEnter \"off\" to exit:\n").lower()
    
    #Case if the user mispelled the given choices or entered anything else other than those mentioned
    if(choice != "latte" and choice != "espresso" and choice != "green tea latte" and choice!="off" and choice!="report"):
           
        while(choice != "latte" and choice != "espresso" and choice != "green tea latte" and choice!="off" and choice!="report") :
            print("Invalid choice.")
            choice = input("What would you like to have? (Latte/Espresso/Green Tea Latte) :").lower()
    
    print() #For 1 line in between
    maker(choice)

print("\nThankyou for purchasing beverage(s)! Have a nice day!\n")