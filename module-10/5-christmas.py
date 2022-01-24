import math
S = []
p = []


def buildTree(i, j, level: int = 0):
    root = S[i][j]
    if root < j:
        buildTree(root + 1, j, level + 1)
        print('\t'*level + p[root][0])
    else:
        buildTree(i, root - 1, level + 1)


def getSum(p):
    s = 0
    for element in p:
        s += element[1]
    return s


def getTree():
    global p
    global S
    arrLength = len(p)
    C = [[[0, 0] for __ in range(arrLength)] for _ in range(arrLength)]
    S = [[0 for __ in range(arrLength)] for _ in range(arrLength)]

    for i in range(arrLength):
        C[i][i] = p[i]

    for nodos in range(1, arrLength):
        for i in range(arrLength - nodos):
            j = i + nodos
            lowest = math.inf
            for r in range(i, j + 1):
                r1 = r - 1
                r2 = r + 1
                item1 = 0 if r1 < 0 else C[i][r1][1]
                item2 = 0 if r2 >= arrLength else C[r2][j][1]
                expr = item1 + item2 + getSum(p[i:j+1])
                if(expr < lowest):
                    lowest = expr
                    S[i][j] = r

            C[i][j] = [0, lowest]

    buildTree(0, arrLength - 1)


def main():
    global p

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
        p = finalArr[i]
        getTree()
        if(i != finalIndex):
            print('')


main()
