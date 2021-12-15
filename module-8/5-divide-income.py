def minFormula(x, total):
    return abs((2*x) - total)


def buildKnapsackMatrix(coinsArr, total):
    totalColumns = int(total/2)
    # totalColumns = total
    coinsLength = len(coinsArr)
    A = [[0 for __ in range(totalColumns + 1)] for _ in range(coinsLength + 1)]

    for i in range(1, coinsLength + 1):
        prevIndex = i - 1
        currentCoin = coinsArr[prevIndex]
        for j in range(totalColumns + 1):
            prevA = A[prevIndex][j]
            if(currentCoin <= j):
                # Logic to set a[i][j]
                x1 = A[prevIndex][j - currentCoin] + currentCoin
                x2 = A[prevIndex][j]
                fx1 = minFormula(x1, total)
                fx2 = minFormula(x2, total)
                A[i][j] = x1 if(fx1 <= fx2) else x2
            else:
                A[i][j] = prevA

    return A


def getMinDifference(arr):
    total = sum(arr)
    A = buildKnapsackMatrix(arr, total)
    # print(A)
    print(minFormula(A[-1][-1], total) * 10)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(int(x) / 10) for x in input().split()])

    for arr in finalArr:
        getMinDifference(arr)


main()
