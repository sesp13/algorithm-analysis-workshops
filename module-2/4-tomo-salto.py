from itertools import permutations


def getBestScore(scoresArr):
    bestScore = 0
    arrLength = len(scoresArr)
    for i in range(arrLength):
        # Create basic combination of 1 and zeros
        negativeArr = [0] * i
        finalArr = [1] * (arrLength - i)
        finalArr.extend(negativeArr)
        # Permute the finalArr
        finalPermuted = permutations(finalArr)
        # Check every case
        for caseArr in finalPermuted:
            score = 0
            for j in range(arrLength):
                if(j == 0):
                    # Check first case
                    score = scoresArr[0] if caseArr[0] == 1 else score
                elif(caseArr[j] == 1):
                    # Common cases
                    if(caseArr[j - 1] == 1):
                        score = score + scoresArr[j] - scoresArr[j-1]
                    else:
                        score += scoresArr[j]

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
