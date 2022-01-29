graph = []
globalLevels = {}


def getScore(level, rowNumber):
    global graph
    global globalLevels

    graphLength = len(graph)
    if(rowNumber > len(graph)):
        return
    # Upgrade level
    level += 1
    conectedNodes = []
    for i in range(1, graphLength):
        coordenate = graph[rowNumber][i]
        if(coordenate == 1):
            if(globalLevels[str(i)] == 'INF' or globalLevels[str(i)] > level):
                # Update level
                globalLevels[str(i)] = level
                conectedNodes.append(i)

    for i in conectedNodes:
        getScore(level, i)


def getPauNumber(arr: object):
    global graph
    global globalLevels
    # Build a graph with this data
    graph = [[0 for __ in range(arr['people'])] for _ in range(arr['people'])]

    for i in range(1, len(graph)):
        globalLevels[str(i)] = 'INF'

    for position in arr['danceArr']:
        graph[position[0]][position[1]] = 1

    # Set levels
    getScore(0, 0)

    for key in globalLevels:
        print(f"{key} {globalLevels[key]}")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        partyArr = input().split(',')
        people = int(partyArr[0])
        dances = int(partyArr[1])
        danceArr = []
        for __ in range(dances):
            danceArr.append([int(x) for x in input().split()])
        finalArr.append({
            "people": people,
            "dances": dances,
            "danceArr": danceArr
        })

    for i in range(cases):
        print(f"fiesta {i + 1}:")
        getPauNumber(finalArr[i])
        if(i != cases - 1):
            print("")


main()
