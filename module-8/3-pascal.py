import math

GLOBALMOD = 999999937

oneMod = 1 % GLOBALMOD

globalPascalArr = [[oneMod], [oneMod, oneMod]]


def buildPascal(maxLevel):
    if(maxLevel <= 2):
        return
    else:
        global globalPascalArr
        global GLOBALMOD
        for level in range(1, maxLevel):
            # Sum 2 because its necesary to build next correct structure
            nextLevel = level + 2
            nextLevelLength = math.ceil(nextLevel / 2)
            currentLevelArr = globalPascalArr[level]
            nextLevelArr = [0 for _ in range(nextLevelLength)]
            # Build new level
            for i in range(1, len(currentLevelArr)):
                prevIndex = i - 1
                sum = currentLevelArr[prevIndex] + currentLevelArr[i]
                nextLevelArr[prevIndex] = sum % GLOBALMOD
            
            # Add final element
            sum = currentLevelArr[-1] + currentLevelArr[-2]
            nextLevelArr[-1] = sum % GLOBALMOD

            globalPascalArr.append(nextLevelArr)


def getPascals(arr: list):
    global globalPascalArr
    maxLevel = max(arr)
    buildPascal(maxLevel)
    print("Hello world")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append(int(input()))

    getPascals(finalArr)


main()
