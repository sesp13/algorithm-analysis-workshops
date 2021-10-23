from itertools import product


def processColorCombination(colorCombination, colorsMatrix):
    numberOfColors = len(colorCombination)
    for i in range(numberOfColors - 1):
        for j in range(i+1, numberOfColors):
            if((colorCombination[i] == colorCombination[j]) and (colorsMatrix[i][j] == 1)):
                return False
    return True


def getColors(numberOfColors, colorsMatrix):
    colors = 1
    while colors < numberOfColors:
        currentColors = [x for x in range(colors)]
        bestCombinationFound = False
        # Get all combination of colors
        colorsCombinated = product(currentColors, repeat=numberOfColors)
        for colorCombination in colorsCombinated:
            if(processColorCombination(colorCombination, colorsMatrix)):
                bestCombinationFound = True
                break
        if(bestCombinationFound):
            break
        colors += 1
    print(colors)


def main():
    cases = int(input())
    finalArray = []
    for i in range(cases):
        numberOfColors = int(input())
        colorsMatrix = []
        for _ in range(numberOfColors):
            # Parse array value
            colorLine = [int(x) for x in input().split()]
            colorsMatrix.append(colorLine)

        finalArray.append([numberOfColors, colorsMatrix])

    for case in finalArray:
        getColors(case[0], case[1])


main()
