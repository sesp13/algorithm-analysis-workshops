def getMaxScore(arr):
    # First case if tge arr length is 1
    arrLength = len(arr)
    if(arrLength == 0):
        print(0)
    elif(arrLength == 1):
        print(arr[0])
    else:
        bestCases = [arr[0]]
        for i in range(1, arrLength):
            # Take or not take
            lastIndex = i - 1
            currentItem = arr[i]
            lastItem = arr[lastIndex]
            bestBefore = bestCases[lastIndex]

            # Choose which is better
            # Take it
            takeScore = bestBefore + currentItem - lastItem
            leaveScore = bestBefore
            bestCases.append(max(takeScore, leaveScore))
        
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
