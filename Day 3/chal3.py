import sys
import re

fileOpen = open('chal3\chal3.txt')
fileRead = fileOpen.read()

lines = fileRead.splitlines()

symbolLocations = []

def SymbolChecking(Map):
    symbols = '*#+=$-&%@/'
    lineNumber = 0
    for line in Map:
        charPosition = 0
        for char in line:
            if char in symbols:
                symbolLocations.append((charPosition, lineNumber))
            charPosition += 1
        lineNumber += 1
    # print(symbolLocations)

    return symbolLocations

def Cheking(Map, SymbolCoords):
    with open('chal3\\numbs1.txt', "w") as outputfile:
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        PartsSum = 0
        PartsFound = []

        lineNumber = 0              # y coord
        for line in Map:
            charPosition = 0        # x coord
            while charPosition < len(line):
                if line[charPosition].isdigit():
                    match = re.match(r'\d+', line[charPosition:]) # Match from the current position

                    if match:
                        number = match.group()  # Extract the full number
                        FullNumberLength = len(number)

                        # Collecting coords
                        Found = False
                        for i in range(FullNumberLength):
                            if Found == False:
                                tempCoords = (charPosition + i, lineNumber)

                                for x, y in directions:
                                    adjacentCoord = (tempCoords[0] + x, tempCoords[1] + y)
                                    if adjacentCoord in SymbolCoords:
                                        # print(f'Symbol found adjacent to {tempCoords}, Part number: {number} the symbol is at {adjacentCoord} from {line[charPosition]}')
                                        # debugging ^
                                        outputfile.write(f'{number}\n')
                                        PartsSum += int(number)
                                        PartsFound.append(number)
                                        Found = True
                                        break
                            else:
                                break
                                
                        charPosition += FullNumberLength # setting the x coord past the length of the number
                        continue  
                charPosition += 1
            lineNumber += 1

        return PartsFound, PartsSum

def ExtractNum(line, charPositionX):
    start = charPositionX
    while start > 0 and line[start - 1].isdigit():
        start -= 1

    end = charPositionX
    while end < len(line) and line[end].isdigit():
        end += 1

    match = line[start:end]
    if match:
        return match, end, start
    return None

def StarChecking(Map):
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    ratios = []
    checked_numbers = set()  # to keep track of checked numbers to avoid redundancy

    for tempCoordsY, line in enumerate(Map):
        for tempCoordsX, val in enumerate(line):
            if val == '*':
                # print(f'* found at {(tempCoordsX, tempCoordsY)}')
                adjacent_numbers = []
                for x, y in directions:
                    newX, newY = tempCoordsX + x, tempCoordsY + y
                    if 0 <= newY < len(Map) and 0 <= newX < len(Map[newY]):
                        if Map[newY][newX].isdigit():
                            number, end, start = ExtractNum(Map[newY], newX)
                            if (newY, start, end) not in checked_numbers:
                                checked_numbers.add((newY, start, end))
                                # print(f'* at {(tempCoordsX, tempCoordsY)} is adjacent to a number at {(newX, newY)} : {number}')
                                adjacent_numbers.append(number)
                if len(adjacent_numbers) > 1:
                    ratio = adjacent_numbers
                    ratios.append(ratio)

    totalSum = 0
    for ratio in ratios:
        product = 1
        for num in ratio:
            product *= int(num)
        totalSum += product

    return ratios, totalSum

print(StarChecking(lines))

#print(Cheking(lines, SymbolChecking(lines)))
