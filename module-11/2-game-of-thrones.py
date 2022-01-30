def getInfo(arr: list):
    families = []
    for register in arr:
        familyFound = False
        for family in families:
            isRegister1 = register[0] in family
            isRegister2 = register[1] in family
            if(isRegister1 or isRegister2):
                familyFound = True
                if(not isRegister1):
                    family.append(register[0])
                if(not isRegister2):
                    family.append(register[1])

        if(not familyFound):
            families.append(register)

    maxNumber = 0
    for family in families:
        maxNumber = max(maxNumber, len(family))

    print(f"{len(families)} {maxNumber}")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        R = int(input())
        caseArr = []
        for __ in range(R):
            caseArr.append([x for x in input().split()])
        finalArr.append(caseArr)

    for arr in finalArr:
        getInfo(arr)


main()
