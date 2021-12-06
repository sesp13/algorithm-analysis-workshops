from sys import stdin, stdout


def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        caseArr = [int(x) for x in stdin.readline().split()]
        arrLength = caseArr[0]
        p = caseArr[1:]
        r1 = [0 for __ in range(arrLength)]
        r2 = [0 for __ in range(arrLength)]
        r1[0] = p[0]
        r2[0] = p[0]
        for i in range(1, arrLength):
            # Set current price for the index
            r1[i] = p[i]
            r2[i] = p[i]
            # Calculate rest
            for j in range(i):
                # Get current price for the index
                pj = p[j]
                # Get the index of the rest pending
                restIndex = i - j - 1
                # Fill for the min proccess
                r1[i] = min(r1[i], pj + r1[restIndex])
                # Fill for the max procceses
                r2[i] = max(r2[i], pj + r2[restIndex])

        lastIndex = arrLength - 1
        stdout.write("{} {}\n".format(
            str(r1[lastIndex]), str(r2[lastIndex])))


main()
