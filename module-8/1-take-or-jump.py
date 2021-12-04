def getMaxScore(arr):
    # First case if tge arr length is 1
    arrLength = len(arr)
    if(arrLength == 0):
        print(0)
    elif(arrLength == 1):
        print(arr[0])
    elif(arrLength == 2):
        print(max(arr))
    else:
        bestCases = [arr[0], max(arr[0], arr[1])]
        for i in range(2, arrLength):
            # Take or not take
            currentItem = arr[i]
            bestBeforeOne = bestCases[i - 1]
            bestBeforeTwo = bestCases[i - 2]
            # Take it
            sumTake = currentItem + bestBeforeTwo
            # Dont take it
            sumNotTake = bestBeforeOne
            bestCases.append(max(sumTake, sumNotTake))

        print(bestCases[arrLength - 1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        caseLength = int(input())
        caseArr = []
        for __ in range(caseLength):
            caseArr.append(int(input()))
        finalArr.append(caseArr)

    for caseArr in finalArr:
        getMaxScore(caseArr)


main()
