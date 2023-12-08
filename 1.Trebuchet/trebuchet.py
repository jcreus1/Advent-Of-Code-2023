import re, csv

def replaceStringDigitsWithNumberDigits(inputString):

  # Attempt 1 doesn't work - input can contain multiple overlapping values e.g. twone
  # processedString = inputString.lower()
  # processedString = processedString.replace("one", "1")
  # processedString = processedString.replace("two", "2")
  # processedString = processedString.replace("three", "3")
  # processedString = processedString.replace("four", "4")
  # processedString = processedString.replace("five", "5")
  # processedString = processedString.replace("six", "6")
  # processedString = processedString.replace("seven", "7")
  # processedString = processedString.replace("eight", "8")
  # processedString = processedString.replace("nine", "9")

  digitDictionary = {
    "one": "1",
    "two": "2", 
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
  }

  processedString = inputString

  # First Word
  earliestIndex = -1
  earliestWord = ""

  # Find first instance of a digit word
  for key in digitDictionary:
    searchValueIndex = processedString.find(key)
  
    if searchValueIndex != -1 and (earliestIndex == -1 or searchValueIndex < earliestIndex):
        earliestIndex = searchValueIndex
        earliestWord = key

  # Replace digit word if found
  if earliestIndex != -1:
    processedString = processedString.replace(earliestWord, digitDictionary[earliestWord], 1)

  # Last word
  latestIndex = -1
  latestWord = ""

  # Find last instance of a digit word
  for key in digitDictionary:
    searchValueIndex = processedString.rfind(key)
  
    if searchValueIndex != -1 and (latestIndex == -1 or searchValueIndex > latestIndex):
        latestIndex = searchValueIndex
        latestWord = key

  # Replace digit word if found
  if latestIndex != -1:
    processedString = processedString[:latestIndex] + digitDictionary[latestWord] + processedString[latestIndex + len(latestWord):]

  return processedString


def readCalibrationValuesFromFile(inputFilePath):
  
  calibrationValues = []

  with open(inputFilePath, "r") as inputFile, open('debug.csv', 'w', newline='') as debugFile:

    debugWriter = csv.writer(debugFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    debugWriter.writerow(['Input Line', 'Processed Line', 'Digits in Line', 'Calibration Value'])

    for inputLine in inputFile:

      processedInputLine = replaceStringDigitsWithNumberDigits(inputLine)
      digitsInLine = re.findall("[0-9]", processedInputLine)

      if len(digitsInLine) == 0:
        continue

      firstValue = digitsInLine[0]
      lastValue = digitsInLine[-1]
      concatenatedValues = str(firstValue) + str(lastValue)

      calibrationValue = int(concatenatedValues)
      calibrationValues.append(calibrationValue)

      debugWriter.writerow([inputLine.strip(), processedInputLine.strip(), ', '.join(digitsInLine), calibrationValue])

  return calibrationValues

calibrationValues = readCalibrationValuesFromFile("1.Trebuchet/input.txt")
print(sum(calibrationValues))