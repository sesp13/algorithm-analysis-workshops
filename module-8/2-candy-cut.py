def getMinMaxCosts(caseArr):
    arrLength = caseArr[0]
    p = caseArr[1:]
    rMax = [p[0]]
    rMin = [p[0]]
    for i in range(1, arrLength):
        # Set current price for the index
        rMax.append(p[i])
        rMin.append(p[i])
        # Calculate rest
        for j in range(i):
            # Get current price for the index
            pj = p[j]
            # Get the index of the rest pending
            restIndex = i - j - 1
            # Fill for the max procceses
            currentMax = rMax[restIndex]
            sumMax = pj + currentMax
            rMax[i] = max(rMax[i], sumMax)
            # Fill for the min proccess
            currentMin = rMin[restIndex]
            sumMin = pj + currentMin
            rMin[i] = min(rMin[i], sumMin)

    print("{} {}".format(rMin[arrLength - 1], rMax[arrLength - 1]))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for caseArr in finalArr:
        getMinMaxCosts(caseArr)


main()
