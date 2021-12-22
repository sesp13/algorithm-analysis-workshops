import math


def getMinBills(arr: list):
    totalColumns = arr[0] + 1
    billsArr = arr[1:]
    arrLength = len(billsArr) + 1
    # Create matrix
    A = [[math.inf for __ in range(totalColumns)] for _ in range(arrLength)]
    # Set initial values for the first column of the matrix
    for i in range(arrLength):
        A[i][0] = 0

    for i in range(1, arrLength):
        prevIndex = i - 1
        currentBill = billsArr[prevIndex]
        for j in range(1, totalColumns):
            prevItem = A[prevIndex][j]
            if(currentBill <= j):
                k = j - currentBill
                A[i][j] = min(1 + A[i][k], prevItem)
            else:
                A[i][j] = prevItem

    print(A[-1][-1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for arr in finalArr:
        getMinBills(arr)


main()
