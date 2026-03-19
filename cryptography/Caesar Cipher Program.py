def main ():
    message = plain_message()
    shift = shift_input()
    encrypted_message= encrypt(message, shift)
    print ("Encrypted Message: " + encrypted_message) 

def plain_message():
    start_message = str(input("Enter the message you want to encrypt: "))
    return start_message
    
def shift_input():
    shift_value= int(input("Enter value to shift: "))
    return shift_value 

def encrypt(message, shift):
    encrypted_message= ""
    #this for loop will go through each letter (i) in the message
    for i in message:
        #this method will check if user input is anything beside a letter
        if i.isalpha():
            #this method will check if letter is uppercase to reset the base count of ASCII number to "A" or 65
            if i.isupper():
                #ordinal command converts a letter into an ASCII number
                control = ord("A")
            #else if the letter is lowercase to reset the base count of ASCII number to "a" or 97
            else:
                #ordinal command converts a letter into an ASCII number
                control = ord("a")
            #this will convert the user input letters into an ASCII number and subtract that by the control value 65 or 97
            #the shift_value is added to the total and then divided by 26 so that the letters will loop at the end of alphabet by the remainder
            shift_message=(ord(i) - control + shift) % 26
            #this will create the new letters by adding the control value back to the shift_message total and converting ASCII numbers back into characters 
            new_letter = chr(shift_message + control)
            #this will add the new letters to build the encrypted message
            encrypted_message += new_letter
        #this will run when no letters are detected like a space
        else:
            #any input that is not letters will stay the same and added back to the encrypted message
            encrypted_message += i
    return encrypted_message
 
main()