import math
currentArr = []


def getMinDistanceSplit(i, j, delta):
    global currentArr
    middleIndex = int((i + j) / 2)
    middlePointX = currentArr[middleIndex][0]
    S = []
    for k in range(i, j +1):
        point = currentArr[k]
        if(abs(point[0] - middlePointX) < delta):
            S.append(point)
    SY = sorted(S, key=lambda element: element[1])
    syLength = len(SY)
    minDistance = delta
    for p in range(syLength - 1):
        q = p + 1
        while q < syLength and q <= p + 7:
            p1 = SY[p]
            p2 = SY[q]
            if(p1[2] != p2[2]):
                currentDistance = math.dist(p1[:2], p2[:2])
                if(currentDistance < minDistance):
                    minDistance = currentDistance
            q += 1
    return minDistance


def getMinDistance(i, j):
    global currentArr
    if(i == j):
        return math.inf
    elif (j-i == 1):
        p1 = currentArr[i]
        p2 = currentArr[j]
        if(p1[2] != p2[2]):
            return math.dist(p1[:2], p2[:2])
        else:
            return math.inf
    else:
        middleIndex = int((i + j) / 2)
        minDistanceLeft = getMinDistance(i, middleIndex)
        minDistanceRight = getMinDistance(middleIndex + 1, j)
        delta = min(minDistanceRight, minDistanceLeft)
        return getMinDistanceSplit(i, j, delta)


def getMinRivalsDistance(caseArr):
    global currentArr
    currentArr = sorted(caseArr, key=lambda element: element[0])
    resultDistance = getMinDistance(0, len(currentArr) - 1)
    if(math.isinf(resultDistance)):
        print('INF')
    else:
        print(round(resultDistance, 1))


def main():
    finalArr = []
    while(True):
        numberOfPlanets = int(input())
        if(numberOfPlanets == 0):
            break
        caseArr = []
        for _ in range(numberOfPlanets):
            inputArr = input().split()
            inputArr[0] = int(inputArr[0])
            inputArr[1] = int(inputArr[1])
            caseArr.append(inputArr)
        finalArr.append(caseArr)

    for caseArr in finalArr:
        getMinRivalsDistance(caseArr)


main()
