from math import dist, inf, floor

currentArr = []


def closestSplitPair(i, j, delta):
    global currentArr
    middleX = currentArr[int((i + j) / 2)][0]
    S = []
    for point in currentArr:
        if(abs(point[0] - middleX) < delta):
            S.append(point)
    S.sort(key=lambda element: element[1])
    SY = S
    minD = delta
    for p in range(len(SY) - 1):
        q = p + 1
        while q < len(SY) and q <= p + 7:
            distance = dist(SY[p], SY[q])
            if(distance < minD):
                minD = distance
            q += 1

    return minD


def closestPair(i, j):
    if(i == j):
        return inf
    elif j - i == 1:
        return dist(currentArr[i], currentArr[j])
    else:
        middle = int((i + j) / 2)
        dl = closestPair(i, middle)
        dr = closestPair(middle + 1, j)
        delta = min(dl, dr)
        return closestSplitPair(i, j, delta)


def getMinDistance(arr):
    global currentArr
    currentArr = sorted(arr, key=lambda element: element[0])
    distance = closestPair(0, len(currentArr) - 1)
    print(round(floor(distance), 0))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        robotsLength = int(input())
        caseArr = []
        for __ in range(robotsLength):
            # [x, y]
            caseArr.append([int(x) for x in input().split()])
        finalArr.append(caseArr)

    for arr in finalArr:
        getMinDistance(arr)


main()
