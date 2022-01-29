graph = []
globalLevels = {}


def getScore(node, level):
    global graph
    global globalLevels

    # Add one level
    level += 1
    if(globalLevels[str(node)]["explored"] == False):
        # New node discovered
        globalLevels[str(node)] = {
            "explored": True,
            "level": level
        }
        # Iterate in the pending nodes
        for i in range(len(graph[node])):
            coordenate = graph[node][i]
            if(coordenate == 1):
                getScore(i, level)

    else:
        # The node has been already used
        # Check which level is lower
        globalLevels[str(node)]["level"] = min(
            level, globalLevels[str(node)]["level"])


def getPauNumber(arr: object):
    global graph
    global globalLevels
    # Build a graph with this data
    graph = [[0 for __ in range(arr['people'])] for _ in range(arr['people'])]
    # Reset global levels
    globalLevels = {}

    for i in range(len(graph)):
        globalLevels[str(i)] = {
            "explored": False,
            "level": 'INF'
        }

    for position in arr['danceArr']:
        graph[position[0]][position[1]] = 1
        graph[position[1]][position[0]] = 1

    # Set levels
    getScore(0, -1)

    for key in globalLevels:
        if(key != "0"):
            print(f"{key} {globalLevels[key]['level']}")


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
