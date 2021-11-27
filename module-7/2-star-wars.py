import math


def getPointDistance(arr, i, j):
    p1 = arr[i]
    p2 = arr[j]
    item1 = math.pow(p1['x'] - p2['x'], 2)
    item2 = math.pow(p1['y'] - p2['y'], 2)
    return math.sqrt((item1 + item2))


def getMinDistanceSplit(arr, i, j, delta):
    middleIndex = int((i + j) / 2)
    middlePointX = arr[middleIndex]['x']
    sxPoints = arr[int(middlePointX - delta): int(middlePointX + delta + 1)]
    syPoints = sorted(sxPoints, key=lambda element: element['y'])
    syLength = len(syPoints)
    minDistance = delta
    for p in range(syLength):
        q = p + 1
        while q < syLength - 1 and q <= p + 7:
            currentDistance = getPointDistance(syPoints, p, q)
            if(currentDistance < minDistance):
                minDistance = currentDistance
            q += 1
    return minDistance


def getMinDistance(arr, i, j):
    if(i == j):
        # A huge number
        return 10000000
    elif (j-i == 1):
        # Function distance
        return getPointDistance(arr, i, j)
    else:
        # Do magic here
        middleIndex = int((i + j) / 2)
        minDistanceLeft = getMinDistance(arr, i, middleIndex)
        minDistanceRight = getMinDistance(arr, 1 + middleIndex, j)
        delta = min(minDistanceRight, minDistanceLeft)
        ds = getMinDistanceSplit(arr, i, j, delta)
        return ds


def getMinRivalsDistance(arr):
    arr = sorted(arr, key=lambda element: element['x'])
    resultDistance = getMinDistance(arr, 0, len(arr) - 1)
    print(resultDistance)


def main():
    finalArr = []
    while(True):
        numberOfPlanets = int(input())
        if(numberOfPlanets == 0):
            break
        caseArr = []
        for _ in range(numberOfPlanets):
            inputArr = input().split()
            planetObject = {
                "x": int(inputArr[0]),
                "y": int(inputArr[1]),
                "team": inputArr[2],
            }
            caseArr.append(planetObject)
        finalArr.append(caseArr)

    for caseArr in finalArr:
        getMinRivalsDistance(caseArr)


main()
