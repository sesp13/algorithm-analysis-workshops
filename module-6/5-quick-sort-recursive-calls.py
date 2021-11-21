# Global var
recursiveCalls = 0


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
        global recursiveCalls
        recursiveCalls += 1
        # Randomly choose a pivot
        p = a
        pivotCorrectIndex = getPivotIndex(arr, a, b, p)
        quickSort(arr, a, pivotCorrectIndex - 1)
        quickSort(arr, pivotCorrectIndex + 1, b)
    return arr


def getRecursiveCalls(arr):
    global recursiveCalls
    quickSort(arr, 0, len(arr) - 1)
    print(recursiveCalls)
    # Reset global var
    recursiveCalls = 0


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        arr = [int(x) for x in input().split()]
        finalArr.append(arr)

    for arr in finalArr:
        getRecursiveCalls(arr)


main()
