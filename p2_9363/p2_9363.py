#Author: Nikolai Ruhe
#Date: 04/13/2018
#Dr. Chan
#AI Class

import Training
import TestData

trainDataFile = raw_input("Please enter the training file name:")
classificationData =  Training.makeBayesianClassifier(trainDataFile)

testingDataFile = raw_input("Please enter the testing file name:")
TestData.test(testingDataFile, classificationData[1], classificationData[0])