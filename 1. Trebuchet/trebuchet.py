import re

def readCalibrationValuesFromFile(inputFilePath):
  calibrationValues = [];

  with open(inputFilePath, "r") as inputFile:

    for inputLine in inputFile:
    
      digitsInLine = re.findall("[0-9]", inputLine)
      numDigitsFound = len(digitsInLine)
      
      if numDigitsFound == 0:
        continue

      firstValue = digitsInLine[0]
      secondValue = digitsInLine[numDigitsFound -1]
      
      stringCalibrationValue = str(firstValue) + str(secondValue)
      calibrationValue = int(stringCalibrationValue)
      calibrationValues.append(calibrationValue)

  return calibrationValues

def sumValues(listOfValues):
  sumTotal = 0
  
  for value in listOfValues:
    sumTotal += value

  return sumTotal

calibrationValues = readCalibrationValuesFromFile("1. Trebuchet\input.txt")
sumOfCalibrationValues = sumValues(calibrationValues)

print(sumOfCalibrationValues)
