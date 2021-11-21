def merge(leftArr, rightArr, length):
    global imperfectionScore
    i = 0
    j = 0
    k = 0
    newArr = []
    leftLength = len(leftArr)
    rightLength = len(rightArr)

    while k < length:
        if(i < leftLength):
            if(j < rightLength):
                if(leftArr[i] <= rightArr[j]):
                    newArr.append(leftArr[i])
                    i += 1
                else:
                    newArr.append(rightArr[j])
                    j += 1
            else:
                # Add left arr
                newArr.extend(leftArr[i:])
                break
        else:
            if(j < rightLength):
                # Add right arr
                newArr.extend(rightArr[j:])
                break
        k += 1
    return newArr


def mergeSort(arr, length):
    length = length if(length == len(arr)) else len(arr)
    if(length > 1):
        newLength = int(length/2)
        leftArr = arr[0:newLength]
        rightArr = arr[newLength:]
        sortedArr = merge(
            mergeSort(leftArr, newLength),
            mergeSort(rightArr, newLength),
            length
        )
        return sortedArr
    else:
        return arr


# arr = ['C', 'C', 'A', 'G', 'T', 'G']
# print(mergeSort(arr, len(arr)))