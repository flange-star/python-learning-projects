#main module, declareVariables
endProgram=str("no")
totalScores=float(0.0) #Float
averageScores=float(0.0) #Float
score =float(0)
number=int(0)
counter=int(0)
#end of declareVariables
while endProgram=="no":
    endProgram=str("no")
    totalScores=float(0.0) #Float
    averageScores=float(0.0) #Float
    score =float(0)
    number=int(0)
    counter=int(0)
    number=int(input("How many students took the test: "))
    for counter in range(1, number+1):
          score=float(input("Enter their score: "))
          totalScores=totalScores+score
          counter=counter+1 #This counter increment was not originally in the pseudocode, I added
    averageScores=int(totalScores/number)
    print ("The average scores is: " + str(averageScores))
    endProgram=str(input("Do you want to end the program? (Enter no to process a new set of test scores)"))

    


