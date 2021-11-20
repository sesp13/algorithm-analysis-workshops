from math import floor
from random import randint


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
    if b - a > 0:
        p = randint(a, b)
        pivotCorrectIndex = getPivotIndex(arr, a, b, p)
        quickSort(arr, a, pivotCorrectIndex - 1)
        quickSort(arr, pivotCorrectIndex + 1, b)
    return arr


def getBestHouse(arr):
    # Sort array
    arrLength = len(arr)
    middle = floor(arrLength / 2)

    # Get correct index
    index = middle - 1 if arrLength % 2 == 0 else middle

    arr = quickSort(arr, 0, arrLength - 1)

    selectedHouse = arr[index]

    diff = 0
    for element in arr:
        if(element != selectedHouse):
            diff += abs(selectedHouse - element)

    print("{} {}".format(selectedHouse, diff))


def main():
    arrLength = int(input())
    arr = []
    for _ in range(arrLength):
        arr.append(int(input()))

    getBestHouse(arr)


main()
