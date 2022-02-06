import heapq
import math


def prim(allCoordenates: list):
    # Create base graph
    graph = {}
    firstCoordenates = allCoordenates.pop()
    graph['0'] = {
        "distance": 0,
        "coord": firstCoordenates,
    }

    # Set values for pq and pendingIds
    pq = [None for _ in range(len(allCoordenates))]
    pendingIds = []
    for i in range(len(allCoordenates)):
        newId = i + 1
        currentCoordenate = allCoordenates[i]
        # Get distance calculated from the coordenates
        distance = math.dist(firstCoordenates, currentCoordenate)
        # Add node to the graph
        graph[newId] = {
            "distance": distance,
            "coord": currentCoordenate,
        }
        # Add node structure to pq
        # Structure is [distance, nodeId]
        pq[i] = [distance, newId]
        # Add Id to pending ids
        pendingIds.append(newId)

    # Make pq a prority queue
    heapq.heapify(pq)
    totalLength = 0

    while(len(pendingIds) > 0):
        # Get popped node
        u = heapq.heappop(pq)
        uId = u[1]
        uNode = graph[uId]

        if(uId in pendingIds):
            # Add u to used nodes
            pendingIds.remove(uId)
            # Add the distance found
            totalLength += uNode['distance']

            # Check the available connections
            for id in pendingIds:
                vNode = graph[id]
                # Calc distance
                distance = math.dist(uNode['coord'], vNode['coord'])
                currentDistance = vNode['distance']
                # Compare and push
                if(distance < currentDistance):
                    vNode['distance'] = distance
                    heapq.heappush(pq, [distance, id])

    print(round(totalLength, 1))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        nodes = int(input())
        caseArr = []
        for __ in range(nodes):
            caseArr.append([float(x) for x in input().split()])
        finalArr.append(caseArr)

    for arr in finalArr:
        prim(arr)


main()
