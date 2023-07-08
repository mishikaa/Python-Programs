def caeser_cipher( choice , message , shift ):
    ''' Function to encrypt the message'''

    shift_text = ""

    if choice == "encode" :
    
        for char in message: #Iterating through each character of the entered message
            shift_ascii = ord(char) + shift #Adding the shift no. in the ascii value of the character
    
            if shift_ascii > 122 : #Case when the ascii value of any character exceeds the ascii value of 'z'
                shift_text += chr(shift_ascii - 122 + 96)
            else : #Case when the ascii value of the character is less than equal to that of 'z'
                shift_text += chr(shift_ascii)
    
        print(f"Encoded message is {shift_text}") #Printing the encoded message using f-string
            
    elif choice == "decode" :
    
        for char in message:
            shift_ascii = ord(char) - shift #Subtracting the shift no. in the ascii value of the character
    
            if shift_ascii < 97 : #Case when the ascii value of any character is less than that of'a'
                shift_text += chr(123 - (97 - shift_ascii))
            else :
                shift_text += chr(shift_ascii)
    
        print(f"Decoded message is {shift_text}") #Printing the decoded message
    
    else : #Case when the user enters something other than 'encode' or 'decode' 
        print("Invalid choice. Try again.") 


print("\n\t\t######### Welcome to ########### ")
import art #importing art.py
print("\t\t###############################\n")

check = "yes"
while check == "yes" :

    message = input( "\nEnter your message : " ).lower()
    choice = input("Enter 'encode' to ENCODE and 'decode' to DECODE : " ).lower()
    shift = int(input( "Type a shift number : "))
    shift %= 25 #This is to make sure it works even for large shift numbers.
    caeser_cipher( choice , message , shift )

    check = input("Type 'yes' to Continue and 'no' to Exit : ").lower()

print("\n############### The program is ended. Thankyou! ################\n")