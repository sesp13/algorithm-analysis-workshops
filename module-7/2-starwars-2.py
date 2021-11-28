from math import dist, inf

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
        p1 = SY[p]
        while q < len(SY) and q <= p + 7:
            p2 = SY[q]
            if(p1[2] != p2[2]):
                distance = dist(p1[:2], p2[:2])
                if(distance < minD):
                    minD = distance
            q += 1

    return minD


def closestPair(i, j):
    if(i == j):
        return inf
    elif j - i == 1:
        global currentArr
        p1 = currentArr[i]
        p2 = currentArr[j]
        if(p1[2] != p2[2]):
            return dist(p1[:2], p2[:2])
        else:
            return inf
    else:
        middle = int((i + j) / 2)
        dl = closestPair(i, middle)
        dr = closestPair(middle + 1, j)
        delta = min(dl, dr)
        return closestSplitPair(i, j, delta)


def getMinRivalsDistance(caseArr):
    global currentArr
    caseArr.sort(key=lambda element: element[0])
    currentArr = caseArr
    resultDistance = closestPair(0, len(currentArr) - 1)
    print(round(resultDistance, 1))


def main():
    finalArr = []
    while(True):
        numberOfPlanets = int(input())
        if(numberOfPlanets == 0):
            break
        caseArr = []
        hasTwoTeams = False
        currentTeam = ''
        for _ in range(numberOfPlanets):
            inputArr = input().split()
            if(currentTeam != inputArr[2]):
                if(currentTeam == ''):
                    currentTeam = inputArr[2]
                else:
                    hasTwoTeams = True
            inputArr[0] = int(inputArr[0])
            inputArr[1] = int(inputArr[1])
            caseArr.append(inputArr)

        finalArr.append([caseArr, hasTwoTeams])

    for element in finalArr:
        if(not element[1]):
            print('INF')
        else:
            getMinRivalsDistance(element[0])


main()
