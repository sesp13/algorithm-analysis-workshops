from math import floor
from random import randint

desiredIndex = 0
desiredContent = -1


def getPivotIndex(arr, a, b, p):
    xa = arr[a]
    xp = arr[p]
    arr[a] = xp
    arr[p] = xa
    i = a
    for j in range(a+1, b + 1):
        if(arr[j] < arr[a]):
            i += 1
            xi = arr[i]
            xj = arr[j]
            arr[i] = xj
            arr[j] = xi

    xi = arr[i]
    xa = arr[a]
    arr[i] = xa
    arr[a] = xi

    return i


def quickSort(arr, a, b):
    global desiredContent
    if b - a > 0:
        # Randomly choose a pivot
        p = randint(a, b)
        pivotCorrectIndex = getPivotIndex(arr, a, b, p)
        if(pivotCorrectIndex == desiredIndex):
            # Stop recursion when the desired pivot is found
            desiredContent = arr[pivotCorrectIndex]
        else:
            quickSort(arr, a, pivotCorrectIndex - 1)
            quickSort(arr, pivotCorrectIndex + 1, b)
    return arr


def getBestHouse(arr):
    global desiredIndex
    global desiredContent

    # Sort array
    arrLength = len(arr)
    middle = floor(arrLength / 2)

    # Get correct index
    index = middle - 1 if arrLength % 2 == 0 else middle
    desiredIndex = index

    # Find desired content using quick sort
    arr = quickSort(arr, 0, arrLength - 1)

    desiredContent = arr[desiredIndex] if(
        desiredContent == -1) else desiredContent

    diff = 0
    for element in arr:
        if(element != desiredContent):
            diff += abs(desiredContent - element)

    print("{} {}".format(desiredContent, diff))


def main():
    arrLength = int(input())
    arr = []
    for _ in range(arrLength):
        arr.append(int(input()))

    getBestHouse(arr)


main()
