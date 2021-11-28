import math


def getPointDistance(arr, i, j):
    p1 = [arr[i][0], arr[i][1]]
    p2 = [arr[j][0], arr[j][1]]
    return math.dist(p1, p2)


def getMinDistanceSplit(arr, i, j, delta):
    middlePointX = arr[int((i + j) / 2)][0]
    sxPoints = [planet for planet in arr if(
        abs(planet[0] - middlePointX) < delta)]
    syPoints = sorted(sxPoints, key=lambda element: element[1])
    syLength = len(syPoints)
    minDistance = delta
    for p in range(syLength - 1):
        q = p + 1
        while q < syLength and q <= p + 7:
            if(syPoints[p][2] != syPoints[q][2]):
                currentDistance = getPointDistance(syPoints, p, q)
                if(currentDistance < minDistance):
                    minDistance = currentDistance
            q += 1
    return minDistance


def getMinDistance(arr, i, j):
    if(i == j):
        # A huge number
        return math.inf
    elif (j-i == 1):
        p1 = arr[i]
        p2 = arr[j]
        if(p1[2] != p2[2]):
            return getPointDistance(arr, i, j)
        else:
            return math.inf
    else:
        # Do magic here
        middleIndex = int((i + j) / 2)
        minDistanceLeft = getMinDistance(arr, i, middleIndex)
        minDistanceRight = getMinDistance(arr, 1 + middleIndex, j)
        delta = min(minDistanceRight, minDistanceLeft)
        return getMinDistanceSplit(arr, i, j, delta)


def getMinRivalsDistance(arr):
    arr = sorted(arr, key=lambda element: element[0])
    resultDistance = getMinDistance(arr, 0, len(arr) - 1)
    if(resultDistance == math.inf):
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
