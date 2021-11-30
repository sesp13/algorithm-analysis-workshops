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
        sum = 0

        # Create result matrix
        final = [[0 for x in range(n)] for y in range(n)] 
        
        for i in range(n):
            for j in range(n):
                value = 0
                if(i < half):
                    if(j < half):
                        # First side P1 P2
                        value = P1[i][j] + P2[i][j]
                        final[i][j] = value
                    else:
                        # Third side P5 P6
                        j1 = j - half
                        value = P5[i][j1] + P6[i][j1]
                        final[i][j] = value
                else:
                    i1 = i - half
                    if(j < half):
                        # Second side P3 P4
                        value = P3[i1][j] + P4[i1][j]
                        final[i][j] = value
                    else:
                        # Fourth side P7 P8
                        j1 = j - half
                        value = P7[i1][j1] + P8[i1][j1]
                        final[i][j] = value

                # Sum current value
                sum += value

        print(sum)
        return final


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
