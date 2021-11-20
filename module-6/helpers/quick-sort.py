from random import randint

# Implements quick sort algorithm


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
        # Randomly choose a pivot
        p = randint(a, b)
        pivotCorrectIndex = getPivotIndex(arr, a, b, p)
        quickSort(arr, a, pivotCorrectIndex - 1)
        quickSort(arr, pivotCorrectIndex + 1, b)
    return arr
