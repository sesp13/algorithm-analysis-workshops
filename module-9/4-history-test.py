import math


def getBestLength(s1: list, s2: list):
    s1Length = len(s1) + 1
    s2Length = len(s2) + 1
    L = [[0 for __ in range(s2Length)] for _ in range(s1Length)]

    for i in range(1, s1Length):
        prevS1Index = i - 1
        currentS1Element = s1[prevS1Index]
        for j in range(1, s2Length):
            prevS2Index = j - 1
            currentS2Element = s2[prevS2Index]
            if(currentS1Element == currentS2Element):
                L[i][j] = L[prevS1Index][prevS2Index] + 1
            else:
                L[i][j] = max(L[prevS1Index][j], L[i][prevS2Index])

    return L[-1][-1]


def calcGrade(correctPoints, totalPoints):
    return int(round(correctPoints / totalPoints * 100, 0))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        caseLength = int(input())
        bestSequence = [x for x in input().split()]
        caseArr = [bestSequence]
        for __ in range(caseLength):
            caseArr.append([x for x in input().split()])
        finalArr.append(caseArr)

    for i in range(cases):
        print(f"caso {i+1}:")
        currentArr = finalArr[i]
        for j in range(1, len(currentArr)):
            correctPoints = getBestLength(currentArr[0], currentArr[j])
            print(calcGrade(correctPoints, len(currentArr[0])))
        if(i != cases - 1):
            print("")


main()
