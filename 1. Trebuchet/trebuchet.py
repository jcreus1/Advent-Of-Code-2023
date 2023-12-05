import re

def readCalibrationValuesFromFile(inputFilePath):
  
  with open(inputFilePath, "r") as inputFile:
    
    calibrationValues = [
      int(str(digitsInLine[0]) + str(digitsInLine[-1]))
      for inputLine in inputFile
      if (digitsInLine := re.findall("[0-9]", inputLine))
    ]
   
  return calibrationValues

calibrationValues = readCalibrationValuesFromFile("1. Trebuchet\input.txt")
print(sum(calibrationValues))