def getMinMaxCosts(caseArr):
    arrLength = caseArr[0]
    p = caseArr[1:]
    rMax = [0 for _ in range(arrLength)]
    rMin = [0 for _ in range(arrLength)]
    rMax[0] = p[0]
    rMin[0] = p[0]
    for i in range(1, arrLength):
        # Set current price for the index
        rMax[i] = p[i]
        rMin[i] = p[i]
        # Calculate rest
        for j in range(i):
            # Get current price for the index
            pj = p[j]
            # Get the index of the rest pending
            restIndex = i - j - 1
            # Fill for the max procceses
            rMax[i] = max(rMax[i], pj + rMax[restIndex])
            # Fill for the min proccess
            rMin[i] = min(rMin[i], pj +  rMin[restIndex])

    lastIndex = arrLength - 1
    print("{} {}".format(rMin[lastIndex], rMax[lastIndex]))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for caseArr in finalArr:
        getMinMaxCosts(caseArr)


main()
