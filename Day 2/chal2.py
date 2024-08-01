import sys
import re

fileOpen = open('chal2.txt')
fileRead = fileOpen.read()

lines = fileRead.splitlines()

redMax = 12
greenMax = 13
blueMax = 14

print(f'the limit is {redMax}, {blueMax}, {greenMax}')

def GameSplit(x):
    GameEntry = x.replace('Game ','')
    GameResult = GameEntry.split(':')
    GameResultHands = GameResult[1]

    #print(f'Checking Game: {GameResult[0]}')

    Ouput = countColors(GameResultHands)
    return Ouput

    # flag = countColors(GameResultHands)
    # if flag == 0:
    #     print(f'Game {GameResult[0]} is possible')
    #     return GameResult[0], 0
    # else:
    #     #print(f'Game {GameResult[0]} is impossible')
    #     return GameResult[0], -1
        


def countColors(x):
    pattern = r'(\d+)\s*(red|blue|green)'
    
    matches = re.findall(pattern, x)

    colorsCount = {'red': 0, 'blue': 0, 'green': 0}

    for quantity, color in matches:
        if colorsCount[color] < int(quantity):
            colorsCount[color] = int(quantity)

    #print(colorsCount)
    # if Checker(colorsCount) == 0:
    #     return 0
    # else:
    #     return -1

    return colorsCount

def Checker(x):

    #print(f'red: {x["red"]}')

    if x['red'] > redMax:
        return -1
    
    #print(f'blue: {x["blue"]}')
    if x['blue'] > blueMax:
        return -1
    
    #print(f'green: {x["green"]}')
    if x['green'] > greenMax:
        return -1
    
    else:
        return 0

def part2():
    # print(f'''

    # file input includes:
    # {lines}
    #     ''')

    total = 0

    for line in lines:
        Output = GameSplit(line)
        total += Output['red'] * Output['green'] * Output['blue']

    print(total)



# def part1():
#     # print(f'''

#     # file input includes:
#     # {lines}
#     #     ''')

#     sum = 0

#     for line in lines:
#         Output = GameSplit(line)
#         if Output[1] == 0:
#             #print(f'Game: {Output[1]} is possible')
#             sum+=int(Output[0])
#         else:
#             #print(f'Game: {Output[1]} is impossible')
#             continue
#     print(sum)



part2()

