import heapq


def getMinCost(array):
    # Create priority queue
    heapq.heapify(array)
    sum = 0
    while True:
        currentLength = len(array)
        if(currentLength >= 2):
            # Normal flow
            firstElement = heapq.heappop(array)
            secondElement = heapq.heappop(array)
            currentSum = firstElement + secondElement
            sum += currentSum
            heapq.heappush(array, currentSum)
        else:
            break
    print(sum)


def main():
    finalArray = []

    while True:
        caseLength = int(input())
        if(caseLength == 0):
            break
        else:
            caseArr = []
            for _ in range(caseLength):
                caseArr.append(int(input()))
            finalArray.append(caseArr)

    for caseArr in finalArray:
        getMinCost(caseArr)


main()
