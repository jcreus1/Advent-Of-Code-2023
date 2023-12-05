import re

calibrationValues = [];

try:
  inputFile = open("input.txt", "r")

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

finally:
  inputFile.close()

sumOfCalibrationValues = 0
for calibrationValue in calibrationValues:
  sumOfCalibrationValues += calibrationValue

print(sumOfCalibrationValues)