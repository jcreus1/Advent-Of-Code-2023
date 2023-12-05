import re

def readCalibrationValuesFromFile(inputFilePath):
  
  with open(inputFilePath, "r") as inputFile:

    for inputLine in inputFile:
    
      digitsInLine = re.findall("[0-9]", inputLine)
      
      if len(digitsInLine) == 0:
        continue

      firstValue = digitsInLine[0]
      lastValue = digitsInLine[-1]
      concatenatedValues = str(firstValue) + str(lastValue)

      calibrationValue = int(concatenatedValues)
      calibrationValues.append(calibrationValue)

  return calibrationValues

calibrationValues = readCalibrationValuesFromFile("1. Trebuchet\input.txt")
print(sum(calibrationValues))