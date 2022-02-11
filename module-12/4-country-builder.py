import heapq
import math
import queue

# Global vars
globalGraph = {}


def getSubGraph(nodeId):
    global globalGraph

    originNode = globalGraph[nodeId]
    originNode['explored'] = True
    # Init current subgraph
    subgraph = {
        nodeId: originNode
    }
    # Begin with BFS
    register = queue.Queue()
    register.put(originNode)
    while (not register.empty()):
        currentNode = register.get()
        for nextRelation in currentNode['related']:
            nextId = nextRelation[1]
            nextNode = globalGraph[nextId]
            if(nextNode['explored'] == False):
                nextNode['explored'] = True
                subgraph[nextId] = nextNode
                # Update register
                register.put(nextNode)

    return subgraph


def prim(subgraph: dict):
    # Get keys
    pendingIds = list(subgraph.keys())
    # Get data from the first id
    firstNode = subgraph[pendingIds[0]]
    firstNode['distance'] = 0
    # Remove first node form pending ids
    del pendingIds[0]
    # Set first values for the pq

    # Set the first node relation's distances
    for relation in firstNode['related']:
        relationId = relation[1]
        nextNode = subgraph[relationId]
        distance = nextNode['distance']
        nextNode['distance'] = min(distance, relation[0])

    # Make pq a priority queue
    pq = [[subgraph[pendingIds[i]]['distance'], pendingIds[i]]
          for i in range(len(pendingIds))]
    heapq.heapify(pq)
    totalSubgraph = 0

    while(len(pendingIds) > 0):
        u = heapq.heappop(pq)
        uId = u[1]
        uNode = subgraph[uId]

        if(uId in pendingIds):
            # Add u to used nodes
            pendingIds.remove(uId)
            # add the distance found
            totalSubgraph += uNode['distance']
            # See the relations of uNode
            for relation in uNode['related']:
                relationId = relation[1]
                # Only do something if this node belongs to pending
                if(relationId in pendingIds):
                    vNode = subgraph[relationId]
                    distance = relation[0]
                    currentDistance = vNode['distance']
                    if(distance < currentDistance):
                        vNode['distance'] = distance
                        # Add vNode to pq
                        heapq.heappush(pq, [distance, relationId])

    return totalSubgraph


def getInfraestructure(arr: list):
    global globalGraph

    # Input vars
    globalGraph = arr[0]
    airportCost = arr[1][2]

    lstSubGraphs = []

    # Get different graphs
    for nodeId in globalGraph:
        currentNode = globalGraph[nodeId]
        if(currentNode['explored'] == False):
            lstSubGraphs.append(getSubGraph(nodeId))

    total = 0
    for subgraph in lstSubGraphs:
        total += prim(subgraph)

    total += (len(lstSubGraphs) * airportCost)

    print(f"{total} {len(lstSubGraphs)}")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        inputArr = [int(x) for x in input().split()]
        cities = inputArr[0]
        possibleConnections = inputArr[1]

        inputGraph = {}
        for i in range(1, cities + 1):
            inputGraph[str(i)] = {
                "related": [],
                "explored": False,
                "distance": math.inf
            }

        for __ in range(possibleConnections):
            connectionArr = [x for x in input().split()]
            origin = connectionArr[0]
            destiny = connectionArr[1]
            cost = int(connectionArr[2])
            # Relation structure [cost, destiny]
            inputGraph[origin]['related'].append([cost, destiny])
            inputGraph[destiny]['related'].append([cost, origin])

        finalArr.append([inputGraph, inputArr])

    for arr in finalArr:
        getInfraestructure(arr)


main()
