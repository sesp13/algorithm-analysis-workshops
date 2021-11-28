import math
hugeNumber = 10000000000000000


def getPointDistance(arr, i, j):
    p1 = arr[i]
    p2 = arr[j]
    item1 = math.pow(p1['x'] - p2['x'], 2)
    item2 = math.pow(p1['y'] - p2['y'], 2)
    return math.sqrt((item1 + item2))


def getMinDistanceSplit(arr, i, j, delta):
    middleIndex = int(math.floor((i + j) / 2))
    sxLeftIndex = i
    sxRightIndex = j + 1
    # Set sxLimits if delta is not hugeNumber
    if(delta != hugeNumber):
        sxLeftIndex = int(math.floor(middleIndex - delta))
        # Sum 1 to take the last frontier
        sxRightIndex = int(math.floor(middleIndex + delta + 1))
    sxPoints = arr[sxLeftIndex: sxRightIndex]
    syPoints = sorted(sxPoints, key=lambda element: element['y'])
    syLength = len(syPoints)
    minDistance = delta
    for p in range(syLength):
        q = p + 1
        while q < syLength and q <= p + 7:
            # Verify if the points are from different groups
            point1 = syPoints[p]
            point2 = syPoints[q]
            if(point1['team'] != point2['team']):
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
        # Verify if the points are from different groups
        point1 = arr[i]
        point2 = arr[j]
        if(point1['team'] != point2['team']):
            # Function distance
            return getPointDistance(arr, i, j)
        else:
            return hugeNumber
    else:
        # Do magic here
        middleIndex = int(math.floor((i + j) / 2))
        minDistanceLeft = getMinDistance(arr, i, middleIndex)
        minDistanceRight = getMinDistance(arr, 1 + middleIndex, j)
        delta = min(minDistanceRight, minDistanceLeft)
        ds = getMinDistanceSplit(arr, i, j, delta)
        return ds


def getMinRivalsDistance(arr):
    arr = sorted(arr, key=lambda element: element['x'])
    resultDistance = getMinDistance(arr, 0, len(arr) - 1)
    if(resultDistance == hugeNumber):
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
