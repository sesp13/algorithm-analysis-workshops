
import heapq
import math

costMatrix = []
distanceMatrix = []
rows = 0
columns = 0


def getRelations(i, j):
    global distanceMatrix
    global rows
    global columns

    prevRow = i - 1
    nextRow = i + 1
    prevColumn = j - 1
    nextColumn = j + 1

    relations = []

    if(prevRow > 0):
        relations.append([distanceMatrix[prevRow][j], [prevRow, j]])

    if(prevColumn > 0):
        relations.append([distanceMatrix[i][prevColumn], [i, prevColumn]])

    if(nextRow < rows):
        relations.append([distanceMatrix[nextRow][j], [nextRow, j]])

    if(nextColumn < columns):
        relations.append([distanceMatrix[i][nextColumn], [i, nextColumn]])

    return relations


def getLowestCost(matrix: list):
    global costMatrix
    global distanceMatrix
    global rows
    global columns

    costMatrix = matrix
    rows = len(costMatrix)
    columns = len(costMatrix[0])

    # Create distanceMatrix
    distanceMatrix = [[math.inf for _ in range(columns)] for __ in range(rows)]
    # Init value
    distanceMatrix[0][0] = 0

    # Create PQ
    pq = []
    heapq.heapify(pq)

    # pq will have [distance, coordenates [i, j]]
    # Add first value
    node = [0, [0, 0]]
    heapq.heappush(pq, node)

    while len(pq) > 0:
        u = heapq.heappop(pq)
        relations = getRelations(u[1][0], u[1][1])

        for nextNode in relations:
            nextSum = u[0] + costMatrix[nextNode[1][0]][nextNode[1][1]]
            if(nextSum < nextNode[0]):
                nextNode[0] = nextSum
                # Update distance matrix
                distanceMatrix[nextNode[1][0]][nextNode[1][1]] = nextSum
                heapq.heappush(pq, nextNode)

    print(distanceMatrix[-1][-1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        inputArr = input().split()
        rowsNumber = int(inputArr[0])
        matrix = []
        for __ in range(rowsNumber):
            matrix.append([int(x) for x in input().split()])
        finalArr.append(matrix)

    for matrix in finalArr:
        getLowestCost(matrix)


main()
