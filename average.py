numberofscores = 0
score = 0
total = 0
average = 0.0
scoreCount = 0
numberOfScores = int(input("please enter the number of scores you want to average: "))

#What python loop structure could we use to repeat the next 3 lines
    score = int(input("please enter a score: "))
    total = total + score
    scoreCount = scoreCount + 1

average = (total) / numberOfScores
print(average)
