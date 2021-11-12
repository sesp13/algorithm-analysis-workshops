def merge(leftArr, rightArr, length):
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
    if(length > 1):
        newLength = int(length/2)
        leftArr = arr[0:newLength]
        rightArr = arr[newLength:]
        sortedArr = merge(
            mergeSort(leftArr, newLength),
            mergeSort(rightArr, newLength),
            length
        )
        resultstr = ''
        for element in sortedArr:
            resultstr += str(element)
        print(resultstr)
        return sortedArr
    else:
        print(arr[0])
        return arr


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        arr = [int(x) for x in input().split()]
        finalArr.append(arr)

    for i in range(cases):
        arr = finalArr[i]
        print("caso {}:".format(i+1))
        mergeSort(arr, len(arr))
        if(i < cases-1):
            print("")


main()
