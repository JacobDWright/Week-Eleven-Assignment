#Test which scores are correct or incorrect
#Jacob Wright
#CIS 125 Week Eleven
#Collaborated with Daniel McMurry and Evan Sauers

from BowlingGame import Game

#Read testcores file
testScores = open("testscores.txt" , "r")
scoresList = []

#Analyze the file
for line in testScores:
    #Strip the lines and split the numbers
    line = line.strip()
    scoresList = line.split(",")
    scoresList = [int(e) for e in scoresList]
    totalScore = scoresList.pop()
    
    g = Game()
    
    #Pins
    for pins in scoresList:
        g.roll(pins)
    score = g.score()
    
    #Print the scores
    print("Your score is {}, but the original score is {}" .format(score, totalScore))
    if score == totalScore:
        print("The score is correct.")
    else:
        print("The score is incorrect, the score should be", score)
        
testScores.close()

#Line number 5 is incorrect