import heapq


def getImperfectionScore(element):
    currentStr = 'current'
    perfectStr = 'perfect'
    orderElement = {
        'A': {currentStr: -1, perfectStr: 1},
        'C': {currentStr: -1, perfectStr: 2},
        'G': {currentStr: -1, perfectStr: 3},
        'T': {currentStr: -1, perfectStr: 4},
    }
    order = 0
    for char in element:
        if(orderElement[char][currentStr] == -1):
            order += 1
            orderElement[char][currentStr] = order
            if(order == 4):
                break

    perfectsRest = 0
    imperfectionScore = 0
    for key in orderElement:
        element = orderElement[key]
        if(element[currentStr] == -1):
            perfectsRest += 1
        else:
            perfection = element[perfectStr] - perfectsRest
            if(perfection != element[currentStr]):
                imperfectionScore += 1

    return imperfectionScore


def getTheBestChosen(arr, chosen):
    pq = []
    heapq.heapify(pq)
    for element in arr:
        score = getImperfectionScore(element)
        criteriaArr = [score, element]
        heapq.heappush(pq, criteriaArr)

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
