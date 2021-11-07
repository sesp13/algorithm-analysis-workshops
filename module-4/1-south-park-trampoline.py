# Each turn lasts 10 min
def getMinKidCryTime(caseArr):
    kids = caseArr[0]

    # Get kids arr sorted by cry time
    kidsArr = sorted(caseArr[1], key=lambda x: x[1], reverse=True)

    # Create distro arr with the times -1 is an empty position
    # This arr will be filled with kid's penalty
    distroArr = [-1] * kids

    cryTime = 0

    for kid in kidsArr:
        # Desired wait time / 10 = desired index
        desiredIdex = int(kid[0] / 10)

        # Look if the desired index is empty
        if(distroArr[desiredIdex] == -1):
            # Desired index empty save child
            distroArr[desiredIdex] = 1
        else:
            # Desired index not empty
            # Begin backtrack process
            while desiredIdex >= 0:
                if(distroArr[desiredIdex] == -1):
                    # Desired index empty save child
                    distroArr[desiredIdex] = 1
                    break
                else:
                    # desiredIdex not empty try with the next one
                    desiredIdex -= 1

            if(desiredIdex < 0):
                # This means that there are not free spaces
                # begin backtrack process until find a free space
                # Set desired index = last index of distro array
                desiredIdex = kids - 1
                # Begin backtrack process
                while desiredIdex >= 0:
                    if(distroArr[desiredIdex] == -1):
                        # Desired index empty save child
                        distroArr[desiredIdex] = 1
                        # Add cry time
                        cryTime += kid[1]
                        break
                    else:
                        # desiredIdex not empty try with the next one
                        desiredIdex -= 1
    print(cryTime)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        kids = int(input())
        kidsArr = []
        for __ in range(kids):
            arr = [int(x) for x in input().split()]
            kidsArr.append(arr)
        finalArr.append([kids, kidsArr])

    for caseArr in finalArr:
        getMinKidCryTime(caseArr)


main()
