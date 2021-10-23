from itertools import product


def getBestScore(scoresArr):
    bestScore = 0
    arrLength = len(scoresArr)
    items = [0, 1]
    itemsCombinated = product(items, repeat=arrLength)
    for caseArr in itemsCombinated:
        score = 0
        for i in range(arrLength):
            if(i == 0):
                # Check first case
                score = scoresArr[0] if caseArr[0] == 1 else score
            elif(caseArr[i] == 1):
                # Common cases
                if(caseArr[i - 1] == 1):
                    score = score + scoresArr[i] - scoresArr[i-1]
                else:
                    score += scoresArr[i]

        # Update best score
        bestScore = score if score > bestScore else bestScore

    print(bestScore)


def main():
    cases = int(input())
    finalArray = []
    for i in range(cases):
        scoresArr = [int(x) for x in input().split()]
        finalArray.append(scoresArr)

    for scoresArr in finalArray:
        getBestScore(scoresArr)


main()
