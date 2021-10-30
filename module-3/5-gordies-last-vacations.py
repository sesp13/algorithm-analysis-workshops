# My time unit is always minutes
# 24h is 1440
# 6h is 360

def hoursToMinutes(hoursStr=''):
    hourArr = [int(hourStr) for hourStr in hoursStr.split(':')]
    return (hourArr[0] * 60) + hourArr[1]


def getDayVisits(dayArr):
    count = 0
    # Sort by the less time to complete
    dayArr = sorted(dayArr, key=lambda x: x[1])

    currentFinishTime = 0
    for task in dayArr:
        if(currentFinishTime == 0):
            # First case
            count += 1
            currentFinishTime = task[1]
        else:
            # Normal flow
            diff = task[0] - currentFinishTime
            if(diff >= 0):
                count += 1
                currentFinishTime += task[1] + diff

    return count


def getMaxVisits(visits):
    saturdayVisits = []
    sundayVisits = []
    mondayVisits = []

    # filter visists array
    for visit in visits:
        # Check basic rules
        beginMinutes = hoursToMinutes(visit[1])
        durationMinutes = int(visit[2])
        finishMinutes = beginMinutes + durationMinutes
        # Visits before 6am (360) are not allowed
        # Visits after 12am (1440) are not allowed
        if not (beginMinutes < 360 or finishMinutes > 1440):
            arrParsed = [beginMinutes, finishMinutes]
            if(visit[0] == 'sabado'):
                saturdayVisits.append(arrParsed)
            elif(visit[0] == 'domingo'):
                sundayVisits.append(arrParsed)
            elif(visit[0] == 'lunes'):
                mondayVisits.append(arrParsed)

    count = 0
    count += getDayVisits(saturdayVisits)
    count += getDayVisits(sundayVisits)
    count += getDayVisits(mondayVisits)
    print(count)


def main():
    cases = int(input())
    finalArray = []
    for _ in range(cases):
        numberOfMembers = int(input())
        caseArr = []
        for __ in range(numberOfMembers):
            caseArr.append([x for x in input().split()])
        finalArray.append(caseArr)

    for visit in finalArray:
        getMaxVisits(visit)


main()
