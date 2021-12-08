import math

GLOBALMOD = 999999937
oneMod = 1 % GLOBALMOD
globalPascalArr = [[oneMod], [oneMod, oneMod]]
globalMaxArr = [oneMod, oneMod]
maxLevel = 0


def buildPascal():
    global maxLevel
    if(maxLevel <= 2):
        return
    else:
        global globalPascalArr
        global globalMaxArr
        global GLOBALMOD
        global oneMod
        for level in range(1, maxLevel - 1):
            nextLevelArr = [oneMod]
            currentLevelArr = globalPascalArr[level]
            # Build new level
            maxSum = 0
            for i in range(1, len(currentLevelArr)):
                prevIndex = i - 1
                sum = currentLevelArr[prevIndex] + currentLevelArr[i]
                maxSum = sum if(sum > maxSum) else maxSum
                nextLevelArr.append(sum % GLOBALMOD)

            # Add final element
            nextLevelArr.append(oneMod)
            # Add best sum
            globalMaxArr.append(maxSum)
            # Add new level to pascal
            globalPascalArr.append(nextLevelArr)


def getPascals(arr: list):
    global globalMaxArr
    global maxLevel
    buildPascal()
    for level in arr:
        print(globalMaxArr[level - 1])

def main():
    global maxLevel
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        level = int(input())
        maxLevel = level if(level > maxLevel) else maxLevel
        finalArr.append(level)

    getPascals(finalArr)


main()
