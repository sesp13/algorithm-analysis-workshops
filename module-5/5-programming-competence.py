import heapq


def addRegisterToDb(exerciseArr, marathonDb):
    team = int(exerciseArr[0])
    exNumber = int(exerciseArr[1])
    minutes = int(exerciseArr[2])
    exResult = exerciseArr[3]

    # Dont count not validable cases
    if(exResult != 'C' and exResult != 'I'):
        return marathonDb

    teamName = "T{}".format(team)
    exNumber = "E{}".format(exNumber)
    currentTeam = marathonDb.get(teamName, -1)
    currentObject = {
        "result": exResult,
        "minutes": minutes
    }

    # Add new team to the db
    if(currentTeam == -1):
        marathonDb[teamName] = {
            exNumber: [currentObject],
            "number": team
        }
    else:
        # Check if the exercise exists
        currentExercise = currentTeam.get(exNumber, -1)
        if(currentExercise == -1):
            currentTeam[exNumber] = [currentObject]
        else:
            lastExercise = currentExercise[len(currentExercise) - 1]
            # Only add a excercise if it wasn't already solved
            if(lastExercise["result"] != 'C'):
                currentExercise.append(currentObject)

    return marathonDb


def printMarathonBoard(db):
    finalQ = []
    heapq.heapify(finalQ)

    for teamNumber in db:
        currentTeam = db[teamNumber]
        exSolved = 0
        penaltyTime = 0
        for exNumber in currentTeam:
            if(exNumber == 'number'):
                continue
            exLst = currentTeam[exNumber]
            exLength = len(exLst)
            # Get last one
            lastEx = exLst[exLength - 1]
            if(lastEx['result'] == 'C'):
                exSolved += 1
                penaltyTime -= lastEx['minutes'] + 20 * (exLength - 1)

        if(exSolved > 0):
            qObject = [exSolved, penaltyTime, currentTeam['number'] * -1]
            heapq.heappush(finalQ, qObject)

    finalLst = []
    for _ in range(len(finalQ)):
        team = heapq.heappop(finalQ)
        teamString = "{} {} {}".format(team[2] * -1, team[0], team[1] * -1)
        finalLst.insert(0, teamString)
    for resultStr in finalLst:
        print(resultStr)


def main():
    cases = int(input())
    finalArr = []
    for i in range(1, cases + 1):
        marathonDb = {}
        numberOfExcercises = int(input())
        for j in range(numberOfExcercises):
            exerciseArr = [x for x in input().split()]
            marathonDb = addRegisterToDb(exerciseArr, marathonDb)

        finalArr.append({
            "number": i,
            "db": marathonDb
        })

    # prevNumber = cases - 1
    for i in range(cases):
        marathon = finalArr[i]
        print("maraton {}:".format(marathon["number"]))
        printMarathonBoard(marathon['db'])
        # Sometimes it works with this
        # if(i != prevNumber):
        #     print(" ")


main()
