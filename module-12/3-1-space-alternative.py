# Just the same code as the original, but here we manage the graph with a direct list
import math


def belmanFord(element: list):
    graph = element[0]
    relations = element[1]

    # Set first node value
    graph[0] = 0

    # Set the other spds
    for _ in range(1, len(relations)):
        for relation in relations:
            originSpd = graph[relation[0]]
            destinySpd = graph[relation[1]]
            cost = relation[2]
            currentSum = originSpd + cost
            if(currentSum < destinySpd):
                # Set new SPD
                graph[relation[1]] = currentSum

    isPossible = False

    for relation in relations:
        originSpd = graph[relation[0]]
        destinySpd = graph[relation[1]]
        cost = relation[2]
        currentSum = originSpd + cost
        if(currentSum < destinySpd):
            isPossible = True
            break

    if(isPossible):
        print('es posible viajar al big bang')
    else:
        print('no es posible')


def main():
    cases = int(input())
    finalArr = []

    for _ in range(cases):
        inputArr = input().split()
        solarSystems = int(inputArr[0])
        wormholes = int(inputArr[1])

        # Create graph
        inputGraph = [math.inf for _ in range(solarSystems)]

        # Create relations
        relationsArr = [[int(x) for x in input().split()]
                        for _ in range(wormholes)]

        finalArr.append([inputGraph, relationsArr])

    for element in finalArr:
        belmanFord(element)


main()
