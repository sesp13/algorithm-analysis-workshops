# Global var counter
counter = 0


def merge(leftArr, rightArr, length):
    global counter
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
                    # Increase counter in leftArr's current length
                    counter += leftLength - i
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


def getCardMoverWinner(arr):

    mergeSort(arr, len(arr))

    if(counter == 0):
        print("Empate")
    elif(counter % 2 == 0):
        print("Pedro")
    else:
        print("Susana")


def main():
    finalArr = []
    while True:
        cases = int(input())
        caseArr = []
        if(cases == 0):
            break
        for _ in range(cases):
            caseArr.append(int(input()))
        finalArr.append(caseArr)

    for arr in finalArr:
        getCardMoverWinner(arr)
        global counter
        counter = 0


main()
