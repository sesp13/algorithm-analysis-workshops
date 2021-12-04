def getMinMaxCosts(caseArr):
    arrLength = caseArr[0]
    p = caseArr[1:]
    rMax = [0 for _ in range(arrLength)]
    rMax[0] = p[0]
    for i in range(1, arrLength):
        rMax[i] = p[i]
        # Calculate rest
        for j in range(i):
            pj = p[j]
            rij = rMax[i - j - 1]
            sum1 = pj + rij
            rMax[i] = max(rMax[i], sum1)

    print(rMax)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for caseArr in finalArr:
        getMinMaxCosts(caseArr)


main()
