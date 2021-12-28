import math


def getMinCost(costArr: list):
    N = len(costArr)
    M = [[0 for __ in range(N)] for _ in range(N)]
    for steps in range(1, N):
        for i in range(N - steps):
            j = i + steps
            lowest = costArr[i][j]
            for k in range(i + 1, j):
                lowest = min(lowest, M[k][j] + M[i][k])
            M[i][j] = lowest

    print(M[0][-1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        parades = int(input())
        caseArr = []
        for i in range(parades):
            currentRow = [x for x in input().split()]
            # Preprocess matrix
            for j in range(parades):
                if(i == j):
                    currentRow[j] = 0
                elif (currentRow[j] == '*'):
                    currentRow[j] = math.inf
                else:
                    currentRow[j] = int(currentRow[j])
            caseArr.append(currentRow)

        finalArr.append(caseArr)

    for arr in finalArr:
        getMinCost(arr)


main()
