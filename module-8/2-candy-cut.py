def getMinMaxCosts(caseArr):
    arrLength = caseArr[0]
    p = caseArr[1:]
    r = [[0, 0] for _ in range(arrLength)]
    # Min 0 Max 1
    r[0] = [p[0], p[0]]
    for i in range(1, arrLength):
        # Set current price for the index
        # Min 0 Max 1
        r[i] = [p[i], p[i]]
        # Calculate rest
        for j in range(i):
            # Get current price for the index
            pj = p[j]
            # Get the index of the rest pending
            restIndex = i - j - 1
            # Fill for the min proccess
            r[i][0] = min(r[i][0], pj + r[restIndex][0])
            # Fill for the max procceses
            r[i][1] = max(r[i][1], pj + r[restIndex][1])

    lastIndex = arrLength - 1
    print("{} {}".format(r[lastIndex][0], r[lastIndex][1]))


def main():
    cases = int(input())
    for _ in range(cases):
        getMinMaxCosts([int(x) for x in input().split()])


main()
