def getSumMatrix(sm1, sm2):
    final = sm1
    count = 0
    length = len(sm1)
    for i in range(length):
        for j in range(length):
            value = sm2[i][j]
            final[i][j] += sm2[i][j]
            count += value

    return final, value


def strassen(n, m1, m2):
    if(n == 1):
        # Base Case
        return [[m1[0][0] * m2[0][0]]]
    else:
        half = int(n / 2)
        # Generate items
        # from m1
        A = [x[:half] for x in m1[:half]]
        B = [x[half:] for x in m1[:half]]
        C = [x[:half] for x in m1[half:]]
        D = [x[half:] for x in m1[half:]]
        # from m2
        E = [x[:half] for x in m2[:half]]
        F = [x[half:] for x in m2[:half]]
        G = [x[:half] for x in m2[half:]]
        H = [x[half:] for x in m2[half:]]

        # Generate subproblems
        P1 = strassen(half, A, E)
        P2 = strassen(half, B, G)
        P3 = strassen(half, A, F)
        P4 = strassen(half, B, H)
        P5 = strassen(half, C, E)
        P6 = strassen(half, D, G)
        P7 = strassen(half, C, F)
        P8 = strassen(half, D, H)

        #  sum submatrixes
        count = 0
        final1 = P1
        final2 = P3
        final3 = P5
        final4 = P7
        count = 0
        length = len(final1)
        
        for i in range(length):
            for j in range(length):
                value1 = P2[i][j]
                value2 = P4[i][j]
                value3 = P6[i][j]
                value4 = P8[i][j]
                final1[i][j] += value1
                final2[i][j] += value2
                final3[i][j] += value3
                final4[i][j] += value4
                # Increase counter
                count += final1[i][j]
                count += final2[i][j]
                count += final3[i][j]
                count += final4[i][j]


        print(count)


def main():
    finalArr = []
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        m1 = []
        m2 = []
        for __ in range(n):
            m1.append([int(x) for x in input().split()])
        for __ in range(n):
            m2.append([int(x) for x in input().split()])
        finalArr.append([n, m1, m2])

    for i in range(cases):
        caseArr = finalArr[i]
        print("caso {}:".format(i + 1))
        strassen(caseArr[0], caseArr[1], caseArr[2])
        if(i != cases - 1):
            print("")


main()
