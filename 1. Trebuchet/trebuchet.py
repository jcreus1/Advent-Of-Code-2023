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

calibrationValues = readCalibrationValuesFromFile("1. Trebuchet\input.txt")
print(sum(calibrationValues))
