#Author: Nikolai Ruhe
#Date: 04/13/2018
#Dr. Chan
#AI Class
import numpy as np
classificationData = []
def makeBayesianClassifier(fileName):
    arffFile = open(fileName, "r")
    outFile = open(fileName+".bin", "w")
    relationData = ""
    attributeDataList = []
    topRates = []
    attributeRates = []
    totalEntries = 0.0
    runningCount = []
    runningCountIndex = 0
    reachedData = False

    #start going through the input file
    for line in arffFile:
        if (reachedData == False):
            if line[0] == '@':
                #create a cursor to input the text
                cursor = 1
                #find out what kind of data element the text is
                defineWord = ""
                while(line[cursor] != ' ' and line[cursor] != '\n'):
                    defineWord += line[cursor]
                    if (cursor < len(line)-1):
                        cursor += 1

                if (defineWord == "relation"):
                    relationData = ""
                    cursor += 1
                    while (line[cursor] != ' ' and line[cursor] != '\n'):
                        relationData += line[cursor]
                        if (cursor < len(line)-1):
                            cursor += 1
                    #print relationData

                #these attributes are really important
                if ( defineWord == "attribute"):
                    attributeData = ""
                    attributeDataType = ""
                    attributeDataList = []
                    cursor += 1
                    while (line[cursor] != ' ' and line[cursor] != '\n'):
                        if (line[cursor] != "'" and line[cursor] != "'" and line[cursor] != " "):
                            attributeDataType += line[cursor]
                        if (cursor < len(line)-1):
                            cursor += 1
                    while (cursor < len(line)):
                        attributeData = ""
                        if (line[cursor] == "{" or line[cursor] == "," or (line[cursor] == " " and line[cursor-1] == ",")):
                            cursor += 1
                            while (line[cursor] != "," and line[cursor] != "}"):
                                if (line[cursor] != "'" and line[cursor] != "'" and line[cursor] != " "):
                                    attributeData += line[cursor]
                                if (cursor < len(line)-1):
                                    cursor += 1
                            attributeDataList.append(attributeData)
                        cursor += 1
                    outFile.write("@attribute " + attributeDataType + " ")
                    for x in range (0, len(attributeDataList)):
                        runningCount.append([])
                        runningCount[runningCountIndex].append(attributeDataList[x])
                        runningCountIndex += 1
                        attributeRates.append([])
                        attributeRates[x].append(attributeDataList[x])
                        outFile.write(attributeDataList[x] + " ")
                    outFile.write("\n")

                if (defineWord == "data"):
                    outFile.write("@lastAttribute " + attributeDataType + " ")
                    for x in range (0, len(attributeDataList)):
                        outFile.write(attributeDataList[x] + " ")
                        for a in range (0, len(runningCount)):
                            runningCount[a].append(0)
                    for a in range (0, len(runningCount)):
                        runningCount[a].append(0)
                    outFile.write("\n")
                    for x in range (0, len(attributeDataList)):
                        topRates.append([])
                        topRates[x].append(attributeDataList[x])
                    reachedData = True

        #here is where all the data gets entered and calculated
        else:
            if (line[0] != "%"):
                totalEntries += 1.0
                lineEntries = 0
                lineString = ""
                testString = ""
                finalAnswer = ""
                minIndex = 0
                for x in range (0, len(line)):
                    if (line[x] != "'" and line[x] != ","):
                        lineString += line[x]
                    elif (line[x] == ","):
                        lineString += ","
                for y in range (0, len(lineString)):
                    if (lineString[y] != "," and lineString[y] != "\n"):
                        testString += lineString[y]
                    elif (lineString[y] == "," or lineString[y] == "\n"):
                        if (lineString[y] == "\n"):
                            finalAnswer = testString
                        for b in range (minIndex, runningCountIndex):
                            if (testString == runningCount[b][0]):
                                minIndex = b
                                for c in range (1, len(attributeDataList)+2):
                                    runningCount[b][c] += 1
                                break
                            elif (testString != runningCount[b][0] and b == runningCountIndex-1):
                                print("Bad input file, some inputs are not expected")
                                exit()
                        testString = ""
                        minIndex += 1
                minIndex = 0

                subtractIndex = -1
                newTestString = ""
                for c in range(0, len(attributeDataList)):
                    if (finalAnswer == attributeDataList[c]):
                        subtractIndex = c+1

                for f in range(0, len(lineString)):
                    if (lineString[f] != "," and lineString[f] != "\n"):
                        newTestString += lineString[f]
                    elif (lineString[f] == "," or lineString[f] == "\n"):
                        for b in range (minIndex, runningCountIndex-len(attributeDataList)):
                            if (newTestString == runningCount[b][0]):
                                minIndex = b
                                for d in range (1, len(attributeDataList)+1):
                                    if (d != subtractIndex):
                                        runningCount[b][d] -= 1
                                break
                        newTestString = ""
                        minIndex += 1

    print(np.matrix(runningCount))
    print("--------------------------------")

    bayesMatrix = runningCount
    finalDataNum = len(attributeDataList)
    rateIndex = 1

    for k in range(len(runningCount)):
        for i in range(len(runningCount[k])):
            if (rateIndex > finalDataNum):
                rateIndex = 1
            if (i == rateIndex and k < len(runningCount)-finalDataNum):
                bayesMatrix[k][i] /= float(runningCount[len(runningCount)-finalDataNum-1+rateIndex][1])
                rateIndex += 1
            if (i == len(runningCount[k])-1):
                bayesMatrix[k][i] /= float(totalEntries)
    print(np.matrix(bayesMatrix))

    outFile.write("@data" + "\n")

    for v in range(len(runningCount)):
        for i in range(len(runningCount[v])):
            outFile.write(str(runningCount[v][i]))
            if (i != len(runningCount[v])-1):
                outFile.write(", ")
        outFile.write("\n")
    classificationData.append(attributeDataList)
    classificationData.append(bayesMatrix)
    return classificationData