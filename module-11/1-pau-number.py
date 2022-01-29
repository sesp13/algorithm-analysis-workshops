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
    for i in range(1, graphLength):
        coordenate = graph[rowNumber][i]
        if(coordenate == 1):
            if(globalLevels[str(i)] == 'INF'):
                # Update level
                globalLevels[str(i)] = level
                getScore(level, i)
            elif(globalLevels[str(i)] > level):
                globalLevels[str(i)] = level


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

    for arr in finalArr:
        print("--")
        getPauNumber(arr)


main()
