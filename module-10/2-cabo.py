import math


def getCabo(p: list):
    arrLength = len(p)
    C = [[0 for __ in range(arrLength)] for _ in range(arrLength)]
    sumP = [[0 for __ in range(arrLength)] for _ in range(arrLength)]

    for i in range(arrLength):
        C[i][i] = p[i]
        sumP[i][i] = p[i]

    if(arrLength > 1):
        for i in range(arrLength - 2, -1, -1):
            for j in range(i + 1, arrLength):
                item1 = sumP[i + 1][j]
                item2 = sumP[i][i]
                sumP[i][j] = item1 + item2

    for nodos in range(1, arrLength):
        for i in range(arrLength - nodos):
            j = i + nodos
            lowest = math.inf
            for r in range(i, j):
                item1 = C[i][r-1]
                item1 = C[r+1][j]
                lowest = min(lowest, item1 + item2 + sumP[i][j])

            C[i][j] = lowest

    print(C[0][-1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for arr in finalArr:
        getCabo(arr)


main()
