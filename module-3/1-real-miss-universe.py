from itertools import permutations


def checkDiags(correctDistro=[]):
    distroLength = len(correctDistro)
    for i in range(distroLength - 1):
        p = 1
        for j in range(i + 1, distroLength):
            if((correctDistro[j] == correctDistro[i] + p) or correctDistro[j] == correctDistro[i] - p):
                return False
            p += 1
    return True


def getNumberOfPossibilities(arr):
    boardLength = arr[0]
    pos1 = [arr[1] - 1, arr[2] - 1]
    pos2 = [arr[3] - 1, arr[4] - 1]
    distros = []
    # index = row
    # value = column
    for x in range(boardLength):
        # Dont count the columns related
        if(x != pos1[1] and x != pos2[1]):
            distros.append(x)

    # Get permutations of distros
    distrosPermuted = permutations(distros)

    count = 0
    for distro in distrosPermuted:
        # Build correct array with the selected
        correctDistro = []
        posUsed = 0
        for row in range(boardLength):
            if(row == pos1[0]):
                correctDistro.append(pos1[1])
                posUsed += 1
            elif(row == pos2[0]):
                correctDistro.append(pos2[1])
                posUsed += 1
            else:
                column = distro[row - posUsed]
                correctDistro.append(column)

        # Check correct distro
        if(checkDiags(correctDistro)):
            count += 1

    print(count)


def main():
    cases = int(input())
    finalArr = []
    for i in range(cases):
        arr = [int(x) for x in input().split()]
        finalArr.append(arr)

    for arr in finalArr:
        getNumberOfPossibilities(arr)


main()
