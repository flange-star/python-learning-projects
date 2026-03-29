#This program allows the user to input their name and then displays 10 random math equations that the user must solve


#import random integers 1-500
import random

#main function includes inputs to start program
def main():

    #declaring the variables
    counter = int(0)
    studentName = str("NO NAME")
    averageRight = float(0.0)
    right = float(0.0)
    number1 = int(0)
    number2 = int(0)
    answer = 0.0
    
    studentName=inputNames()
    while counter < 10: #counts the number of questions being asked 
        number1, number2 = getNumbers()
        answer = getAnswer(number1, number2)
        right=checkAnswer(number1,number2,right,answer)
        counter = counter + 1
    averageRight = right / 10 
    displayInfo(studentName,right,averageRight)

#function allows user to input their name
def inputNames():
    studentName=str(input("Enter Student Name: "))
    return studentName

#function retrieves random integers from 1-500
def getNumbers():
    number1 = (random.randint(1, 500))
    number2 = (random.randint(1, 500))
    return number1, number2

#function prints questions for user to input answer for sum
def getAnswer(number1, number2):
    print("What is the answer to the following equation")
    print(number1)
    print("+")
    print(number2)
    answer = int(input("What is the sum: "))
    return answer

#function diagnoses user's input answer as right or wrong and counts the amount of questions right
def checkAnswer(number1, number2,right,answer):
    if answer==number1+number2:
        print("Right")
        right=right+1
    else:
        print("Wrong")
    return right

#function outputs the user's name, the number of questions right, and the average number right of  10 questions
def displayInfo(studentName, right,averageRight):
    print("Information for student: " + str(studentName))
    print("The number right: " + str(int(right))) 
    print("The average right is: " + str(averageRight) + " or " + "{:.0%}".format(averageRight))

#calls the main() function to run program 
main()


    
