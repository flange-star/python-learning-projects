#This program allows the user to input the number of students that have taken a test and their scores, and then displays the average of the scores

#main function includes inputs to start program
def main():
    endProgram,totalScores,averageScores,score,number,counter=declareVariables()
    while endProgram=="no": 
        endProgram,totalScores,averageScores,score,number,counter=declareVariables()
        number=getNumber()
        for counter in range(1, number+1): #creates the range for number of scores
            score=getScores()
            totalScores=totalScores+score
            counter=counter+1
        averageScores=getAverage(totalScores,number)
        printAverage(averageScores)
        endProgram=str(input("Do you want to end the program? (Enter no to process a new set of test scores)"))

#function declares the variables      
def declareVariables():
    endProgram=str("no")
    totalScores=float(0.0) 
    averageScores=float(0.0) 
    score =float(0)
    number=int(0)
    counter=int(0)
    return endProgram,totalScores,averageScores,score,number,counter

#function asks user for input of how many tests were taken
def getNumber():
    number=int(input("How many students took the test: "))
    return number

#function asks user to input scores of test depending on how many students took the test
def getScores():
        score=float(input("Enter their score: "))
        return score

#function calculates average score of combined total of student test scores
def getAverage(totalScores,number):
    averageScores=int(totalScores/number)
    return averageScores

#function outputs the average score of the tests
def printAverage(averageScores):
    print ("The average scores is: " + str(averageScores))

#calling the main() function to run program
main()


        
        
            
            
            
    
    


    

    
    
    
    
    


    


