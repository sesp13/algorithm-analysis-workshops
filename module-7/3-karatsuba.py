def getKaratsuba(n, number1, number2):
    if(n == 1):
        resultNumber = int(number1) * int(number2)
        print(resultNumber)
        return str(resultNumber)
    else:
        half = int(n / 2)
        a = number1[:half]
        b = number1[half:]
        c = number2[:half]
        d = number2[half:]

        P1 = int(getKaratsuba(half, a, c))
        P2 = int(getKaratsuba(half, a, d))
        P3 = int(getKaratsuba(half, b, c))
        P4 = int(getKaratsuba(half, b, d))

        resultNumber = ((10**n) * P1) + \
            ((10**half) * (P2 + P3)) + P4

        print(resultNumber)
        return str(resultNumber)


def main():
    cases = int(input())
    finalArr = []
    caseCount = 1
    for _ in range(cases):
        arr = [x for x in input().split()]
        finalArr.append([caseCount, arr])
        caseCount += 1

    for i in range(len(finalArr)):
        item = finalArr[i]
        print("caso {}:".format(item[0]))
        n = int(item[1][0])
        n1 = item[1][1]
        n2 = item[1][2]
        getKaratsuba(n, n1, n2)
        if(i != cases - 1):
            print("")


main()
