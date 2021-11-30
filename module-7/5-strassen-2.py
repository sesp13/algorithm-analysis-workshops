def strassen(n, m1, m2):
    if(n == 2):
        a = m1[0][0]
        b = m1[0][1]
        c = m1[1][0]
        d = m1[1][1]

        e = m2[0][0]
        f = m2[0][1]
        g = m2[1][0]
        h = m2[1][1]

        # Base Case
        sum =  a*e + b*g + a*f + b*h + c*e + d*g + c*f + d*h
        print(sum)
        return sum
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

        # Sum all the components from the matrix
        sum = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8

        print(sum)
        return sum


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
