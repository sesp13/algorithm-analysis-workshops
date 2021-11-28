import math
hugeNumber = 100000


def getPointDistance(arr, i, j):
    global hugeNumber
    p1 = arr[i]
    p2 = arr[j]
    if(p1['team'] != p2['team']):
        item1 = math.pow(p1['x'] - p2['x'], 2)
        item2 = math.pow(p1['y'] - p2['y'], 2)
        return round(math.sqrt((item1 + item2)), 1)
    else:
        return hugeNumber


def getMinDistanceSplit(arr, i, j, delta):
    middleIndex = int((i + j) / 2)
    sxLeftIndex = int(middleIndex - delta)
    sxRightIndex = int(middleIndex + delta)
    sxPoints = arr[sxLeftIndex: sxRightIndex]
    syPoints = sorted(sxPoints, key=lambda element: element['y'])
    syLength = len(syPoints)
    minDistance = delta
    for p in range(syLength):
        q = p + 1
        while q < syLength and q <= p + 7:
            currentDistance = getPointDistance(syPoints, p, q)
            if(currentDistance < minDistance):
                minDistance = currentDistance
            q += 1
    return minDistance


def getMinDistance(arr, i, j):
    if(i == j):
        # A huge number
        return hugeNumber
    elif (j-i == 1):
        return getPointDistance(arr, i, j)
    else:
        # Do magic here
        middleIndex = int((i + j) / 2)
        minDistanceLeft = getMinDistance(arr, i, middleIndex)
        minDistanceRight = getMinDistance(arr, 1 + middleIndex, j)
        delta = min(minDistanceRight, minDistanceLeft)
        return getMinDistanceSplit(arr, i, j, delta)


def getMinRivalsDistance(arr):
    arr = sorted(arr, key=lambda element: element['x'])
    resultDistance = getMinDistance(arr, 0, len(arr) - 1)
    if(resultDistance == hugeNumber):
        print('INF')
    else:
        print(resultDistance)
        # print(round(resultDistance, 1))


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
