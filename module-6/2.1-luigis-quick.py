from math import floor
from random import randint

# Version of the exercise using quick sort -> statitic k

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


def findStatistic(arr, i, j, k):
    if(i == j):
        return arr[i]
    else:
        p = randint(i, j)
        h = getPivotIndex(arr, i, j, p)
        if(k == h):
            return arr[h]
        elif k > h:
            return findStatistic(arr, h+1, j, k)
        else:
            return findStatistic(arr, i, h-1, k)


def getBestHouse(arr):
    arrLength = len(arr)
    middle = floor(arrLength / 2)

    # Get correct index
    index = middle - 1 if arrLength % 2 == 0 else middle

    selectedHouse = findStatistic(arr, 0, arrLength - 1, index)

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
