import math


def getCabo(p: list):
    arrLength = len(p)
    C = [[0 for __ in range(arrLength)] for _ in range(arrLength)]

    for i in range(arrLength):
        C[i][i] = p[i]

    for nodos in range(1, arrLength):
        for i in range(arrLength - nodos):
            j = i + nodos
            lowest = math.inf
            for r in range(i, j + 1):
                r1 = r - 1
                r2 = r + 1
                item1 = 0 if r1 < 0 else C[i][r1]
                item2 = 0 if r2 >= arrLength else C[r2][j]
                lowest = min(lowest, item1 + item2 + sum(p[i:j+1]))

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
