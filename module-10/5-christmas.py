import math
S = []
lights = []


def buildTree(i, j, level: int = 0):
    global S
    global lights
    
    root = S[i][j]

    if root < j:
        buildTree(root + 1, j, level + 1)

    print('\t'*level + lights[root][0])

    if i < root:
        buildTree(i, root - 1, level + 1)


def getSum(p):
    s = 0
    for element in p:
        s += element[1]
    return s


def getTree():
    global lights
    global S
    arrLength = len(lights)
    C = [[0 for __ in range(arrLength)] for _ in range(arrLength)]
    S = [[0 for __ in range(arrLength)] for _ in range(arrLength)]

    for i in range(arrLength):
        C[i][i] = lights[i][1]

    for nodos in range(1, arrLength + 1):
        for i in range(arrLength - nodos + 1):
            j = i + nodos - 1
            lowest = math.inf
            currentSum = getSum(lights[i:j+1])
            for r in range(i, j + 1):
                r1 = r - 1
                r2 = r + 1
                item1 = 0 if r1 < 0 else C[i][r1]
                item2 = 0 if r2 >= arrLength else C[r2][j]
                expr = item1 + item2 + currentSum
                if(expr < lowest):
                    lowest = expr
                    S[i][j] = r

            C[i][j] = lowest

    buildTree(0, arrLength - 1)


def main():
    global lights

    cases = int(input())
    finalArr = []
    for _ in range(cases):
        caseArr = []
        for element in input().split():
            item = element.split(':')
            caseArr.append([item[0], int(item[1])])

        finalArr.append(caseArr)

    finalIndex = len(finalArr) - 1
    for i in range(len(finalArr)):
        print(f"caso {i + 1}:")
        print('')
        lights = finalArr[i]
        lights.sort()
        getTree()
        if(i != finalIndex):
            print('')


main()
