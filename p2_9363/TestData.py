#Author: Nikolai Ruhe
#Date: 04/13/2018
#Dr. Chan
#AI Class

import numpy as np
def test(fileName, bayesMatrix, endList):
    inputFile = open(fileName, "r")
    outfile = open(fileName + ".CONFUSION", "w")
    confusionMatrix = []
    options = len(endList)

    for t in range(0, len(endList)):
        confusionMatrix.append([])
        for w in range(0, len(endList)):
            confusionMatrix[t].append(0)

    predictionArray = []
    for x in range(0, len(endList)):
        predictionArray.append(1)
    reachedData = False
    for line in inputFile:
        if (reachedData == False):
            if (line[0] == "@"):
                # create a cursor to input the text
                cursor = 1
                # find out what kind of data element the text is
                defineWord = ""
                while (line[cursor] != ' ' and line[cursor] != '\n'):
                    defineWord += line[cursor]
                    if (cursor < len(line) - 1):
                        cursor += 1
                if (defineWord.__contains__("data")):
                    reachedData = True
        else:
            testData = ""
            finalAnswer = ""
            minIndex = 0
            for a in range(0, len(line)):
                if (line[a] != "," and line[a] != "\n"):
                    testData += line[a]
                elif (line[a] == "," or line[a] == "\n"):
                    if (line[a] == "\n"):
                        finalAnswer = testData
                    else:
                        for b in range(minIndex, len(bayesMatrix)-options):
                            if (testData == bayesMatrix[b][0]):
                                minIndex = b
                                for c in range(0, len(predictionArray)):
                                    predictionArray[c] *= bayesMatrix[b][c+1]
                                break
                        testData = ""
                        minIndex += 1
            minIndex = 0
            maxIndex = -1
            for j in range(0, options):
                if (j == 0):
                    maxIndex = 0
                elif(predictionArray[j] > predictionArray[maxIndex]):
                    maxIndex = j

            for k in range(0, options):
                if (finalAnswer.__contains__(endList[k])):
                    for m in range(0, options):
                        if (endList[m].__contains__(endList[maxIndex])):
                            confusionMatrix[k][m] += 1

    print(np.matrix(confusionMatrix))
    printString = ""
    outfile.write("         Predicted:" + "\n")
    outfile.write("Actual:" + "\n")
    for e in range(0, options):
        spaces = 9 - len(endList[e])
        outfile.write(endList[e])
        for u in range(0, spaces):
            outfile.write(" ")
        for f in range(0, options):
            outfile.write(str(confusionMatrix[e][f]) + "  ")
        outfile.write("\n")
