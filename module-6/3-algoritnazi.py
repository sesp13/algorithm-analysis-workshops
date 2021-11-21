import heapq

# Global var counter
imperfectionScore = 0


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
                    # Increase counter in leftArr's current length
                    imperfectionScore += leftLength - i
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


def setImperfectionScore(element):
    # Convert the char into an element also apply merge sort which modify global's
    # imperfection score
    elementArr = []
    for elementChar in element:
        elementArr.append(elementChar)
    mergeSort(elementArr, len(elementArr))


def getTheBestChosen(arr, chosen):
    global imperfectionScore
    pq = []
    heapq.heapify(pq)
    for element in arr:
        # The key is by finding array inversions!
        setImperfectionScore(element)
        # Use global var imperfectionScore
        criteriaArr = [imperfectionScore, element]
        heapq.heappush(pq, criteriaArr)
        # Reset imperfection score for the next case
        imperfectionScore = 0

    for _ in range(chosen):
        chosenElement = heapq.heappop(pq)
        print(chosenElement[1])


def main():
    inputArr = input().split()
    totalOfElements = int(inputArr[0])
    chosen = int(inputArr[1])

    finalArr = []
    for _ in range(totalOfElements):
        finalArr.append(input())

    # print('-------')
    getTheBestChosen(finalArr, chosen)


main()
