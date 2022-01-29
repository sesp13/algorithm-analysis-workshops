def getPauNumber(arr: object):
    # Reset global levels
    globalLevels = {}

    # Create dict structure
    for i in range(arr['people']):
        globalLevels[str(i)] = {
            "level": 'INF',
            "related": []
        }

    # Fill the dictionary with the relations
    for dance in arr["danceArr"]:
        related1 = globalLevels[str(dance[0])]['related']
        # Add in current related
        if(dance[1] not in related1):
            related1.append(str(dance[1]))

        # Also add it in the related node related array
        related2 = globalLevels[str(dance[1])]['related']
        if(dance[0] not in related2):
            related2.append(str(dance[0]))

    # Set base case
    level = 1
    nextLevelItems = globalLevels['0']['related']
    globalLevels['0']['level'] = 0

    while True:
        newNextLevels = []
        for index in nextLevelItems:
            node = globalLevels[index]
            # Set current levels
            if(node['level'] == 'INF'):
                node['level'] = level
            # Add new next levels
            for newNode in node['related']:
                if(newNode not in newNextLevels and globalLevels[newNode]['level'] == 'INF'):
                    newNextLevels.append(newNode)

        if(len(newNextLevels) == 0):
            break
        else:
            level += 1
            nextLevelItems = newNextLevels

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
