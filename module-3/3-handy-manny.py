def getMinBill(arr):
    numberOfTasks = arr[0]
    tasks = arr[1:]
    # [weight, taskIndex]
    weightMatrix = []
    for i in range(numberOfTasks):
        # Penalty / Time
        weight = tasks[i][1] / tasks[i][0]
        weightMatrix.append([weight, i])
    
    # sortWeightMatrix
    weightMatrix = sorted(weightMatrix, reverse=True)

    currentTime = 0
    bill = 0
    for weightItem in weightMatrix:
        task = tasks[weightItem[1]]
        currentTime += task[0]
        penaltyTime = currentTime - task[0]
        bill += penaltyTime * task[1]

    print(bill)


def main():
    cases = int(input())
    finalArray = []
    for _ in range(cases):
        caseArr = []
        numberOfTasks = int(input())
        caseArr.append(numberOfTasks)
        for __ in range(numberOfTasks):
            caseArr.append([int(x) for x in input().split()])
        finalArray.append(caseArr)

    for arr in finalArray:
        getMinBill(arr)


main()
