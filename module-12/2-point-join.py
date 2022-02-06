import heapq
import math


def prim(allCoordenates: list):

    # createCoordenates

    # Set initial nodes
    # Structure
    # [cost, coordenates]

    graph = {}
    firstCoordenates = allCoordenates.pop()
    graph['0'] = {
        "distance": 0,
        "coord": firstCoordenates,
    }

    pq = [None for _ in range(len(allCoordenates))]
    pendingIds = []
    # Set the rest of nodes
    for i in range(len(allCoordenates)):
        newId = i + 1
        currentCoordenates = allCoordenates[i]
        # Distance calculated from the coordenates
        distance = math.dist(firstCoordenates, currentCoordenates)
        # Add node to the graph
        graph[newId] = {
            "distance": distance,
            "coord": currentCoordenates,
        }
        # Add node structure to pq
        # Structure [distance, nodeId]
        pq[i] = [distance, newId]
        # Id to pending ids
        pendingIds.append(newId)

    # Make pq a prority queue
    heapq.heapify(pq)

    totalLength = 0

    while(len(pendingIds) > 0):
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
                if(distance < currentDistance):
                    vNode['distance'] = distance
                    heapq.heappush(pq, [distance, id])

    print(totalLength)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        nodes = int(input())
        caseArr = []
        for __ in range(nodes):
            # Add point
            caseArr.append([float(x) for x in input().split()])
        finalArr.append(caseArr)

    for arr in finalArr:
        prim(arr)


main()
