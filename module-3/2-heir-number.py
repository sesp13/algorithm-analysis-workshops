from itertools import permutations


def isHeirNumber(number):
    numberStr = str(number)
    numberArr = [x for x in numberStr]
    totalOfDigits = len(numberArr)

    # Check first clause: pair digits
    if (totalOfDigits % 2 != 0):
        print("No")
        return

    arrPermutations = permutations(numberArr)

    for arrPermuted in arrPermutations:
        # Build number pairs
        number1 = ''
        number2 = ''
        for i in range(totalOfDigits):
            if(i < totalOfDigits/2):
                number1 += arrPermuted[i]
            else:
                number2 += arrPermuted[i]

        number1 = int(number1)
        number2 = int(number2)

        # Check multiplication rule
        if(number1 * number2 == number):
            print("Heredero")
            return

    # There was not a valid permutation
    print("No")
    return


def main():
    cases = int(input())
    finalArr = []
    for i in range(cases):
        finalArr.append(int(input()))

    for number in finalArr:
        isHeirNumber(number)


main()
