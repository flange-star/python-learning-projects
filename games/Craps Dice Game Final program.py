#This program allows the user to play the game of Craps until they quit to reveal the amount of rounds won and lost

#import random integers 1-6
import random

def main():
#declaring the variables
    die_1=int(0)
    die_2=int(0)
    die_a=int(0)
    die_b=int(0)
    win_total=int(0)
    lose_total=int(0)
    roll_total=die_1 + die_2
    next_total=die_a + die_b
    end_program=str('Y')
    
#this loop will run program again depending on user input
    while end_program=="Y":
        die_1,die_2,roll_total= dice_numbers()
        win_total,lose_total=roll_dice(roll_total,win_total,lose_total)
        end_program= str(input("\n"+"Would you like to play a new game? [Y or N]: "))
        print ("\n")
#count_total function will print out the total amount of wins and losses
    count_total(win_total,lose_total)
                
def dice_numbers():
#assigns each die with a random integer and prints the respective faces
    die_1=(random.randint(1,6))
    die_2=(random.randint(1,6))
    roll_total=die_1+die_2
    print("Dice 1 rolled : " + str(die_1))
    die_1_faces(die_1)
    print("Dice 2 rolled : " + str(die_2))
    die_2_faces(die_2)
    return die_1,die_2, roll_total

def roll_dice(roll_total,win_total,lose_total):
#this loop compares the rolled die with the total integer needed to win or lose 
    # a total roll of 7 or 11 is a win and adds a win to the win_total
    if roll_total == 7 or roll_total==11:
        print("The roll came out to: " + str(roll_total))
        print ("You win!")
        win_total=win_total+1
    #a roll of 2,3, or 12 is a loss and adds a loss to the lose_total
    elif roll_total == 2 or roll_total==3 or roll_total==12:
        print("The roll came out to: " + str(roll_total))
        print("You lose.")
        lose_total=lose_total+1
    #any roll other than the above will lead program to the next_round function
    else:
        print("The roll came out to: " + str(roll_total)+"\n")
        print("You must keep rolling until you roll a combined " + str(roll_total)+ " in order to win! If you roll a combined 7, you lose."+"\n")
        win_total,lose_total=next_round(win_total,lose_total,roll_total)
    return win_total,lose_total

def next_round(win_total,lose_total,roll_total):
#This loop allows the game to continue into a second round until either the original total is rolled, a win, or a 7 is rolled, a loss.
    next_roll=str("Y")
    print("The second round will now begin!")
    play=str(input("Press Enter to begin!"+"\n"))
    while next_roll=='Y':
#assigns each die with a random integer and prints the respective faces
        die_a=(random.randint(1,6))
        die_b=(random.randint(1,6))
        next_total= die_a+die_b
        print("Dice 1 rolled : " + str(die_a))
        die_a_faces(die_a)
        print("Dice 2 rolled : " + str(die_b))
        die_b_faces(die_b)
        #if the roll comes out to 7 you lose and a loss is added to the lose_total
        if next_total==7:
            print("The roll came out to: " + str(next_total))
            print("You lost, better luck next time"+"\n")
            lose_total=lose_total+1
            next_roll='N'
        #if the new roll comes out to the same number as the orignal die pair then you won and a win is added to the win_total
        elif next_total==roll_total:
            print("The roll came out to: " + str(next_total))
            print ("You won!"+"\n")
            win_total=win_total+1
            next_roll='N'
        #any roll other than above will lead the program to loop again until you either win or lose
        else:
            print("The roll came out to: " + str(next_total))
            print("The roll is still set to the original roll of: " + str(roll_total)+"\n")
    return win_total,lose_total    
    

def face_1():
    print("┌─────────┐")
    print("│         │")
    print("│    ●    │")
    print("│         │")
    print("└─────────┘")
    
def face_2():
    print("┌─────────┐")
    print("│  ●      │")
    print("│         │")
    print("│      ●  │")
    print("└─────────┘")
    
def face_3():
    print("┌─────────┐")
    print("│  ●      │")
    print("│    ●    │")
    print("│      ●  │")
    print("└─────────┘")
    
def face_4():
    print("┌─────────┐")
    print("│  ●   ●  │")
    print("│         │")
    print("│  ●   ●  │")
    print("└─────────┘")
    
def face_5():
    print("┌─────────┐")
    print("│  ●   ●  │")
    print("│    ●    │")
    print("│  ●   ●  │")
    print("└─────────┘")
    
def face_6():
    print("┌─────────┐")
    print("│  ●   ●  │")
    print("│  ●   ●  │")
    print("│  ●   ●  │")
    print("└─────────┘")

def die_1_faces(die_1):
#this loop determines each respective face for first dice 
    if die_1==1:
        face_1()
    elif die_1==2:
        face_2()
    elif die_1==3:
        face_3()
    elif die_1==4:
        face_4()
    elif die_1==5:
        face_5()
    elif die_1==6:
        face_6()

def die_2_faces(die_2):
#this loop determines each respective face for second dice 
    if die_2==1:
        face_1()
    elif die_2==2:
        face_2()
    elif die_2==3:
        face_3()
    elif die_2==4:
        face_4()
    elif die_2==5:
        face_5()
    elif die_2==6:
        face_6()

def die_a_faces(die_a):
#this loop determines each respective face for first dice in second round
    if die_a==1:
        face_1()
    elif die_a==2:
        face_2()
    elif die_a==3:
        face_3()
    elif die_a==4:
        face_4()
    elif die_a==5:
        face_5()
    elif die_a==6:
        face_6()
        
def die_b_faces(die_b):
#this loop determines each respective face for second dice in second round
    if die_b==1:
        face_1()
    elif die_b==2:
        face_2()
    elif die_b==3:
        face_3()
    elif die_b==4:
        face_4()
    elif die_b==5:
        face_5()
    elif die_b==6:
        face_6()

def count_total(win_total,lose_total):
#prints the total number of losses and wins
    print("Number of wins: " + str(win_total))
    print("Number of losses: " + str(lose_total))



#Input main program here
main()

