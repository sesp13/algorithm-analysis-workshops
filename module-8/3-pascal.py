import math

GLOBALMOD = 999999937

oneMod = 1 % GLOBALMOD

globalPascalArr = [[oneMod], [oneMod, oneMod]]
# globalPascalArr = [[1], [1, 1]]


def buildPascal(maxLevel):
    if(maxLevel <= 2):
        return
    else:
        global globalPascalArr
        global GLOBALMOD
        global oneMod
        for level in range(1, maxLevel - 1):
            nextLevelArr = [oneMod]
            currentLevelArr = globalPascalArr[level]
            # Build new level
            for i in range(1, len(currentLevelArr)):
                prevIndex = i - 1
                sum = currentLevelArr[prevIndex] + currentLevelArr[i]
                nextLevelArr.append(sum % GLOBALMOD)

            # Add final element
            nextLevelArr.append(oneMod)

            globalPascalArr.append(nextLevelArr)


def getPascals(arr: list):
    global globalPascalArr
    maxLevel = max(arr)
    buildPascal(maxLevel)
    print(3 % GLOBALMOD)
    print("Hello world")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append(int(input()))

    getPascals(finalArr)


main()
