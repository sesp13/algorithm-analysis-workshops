import math
S = []
result = ''

def getParenthesis(i, j):
    global result
    if(i == j):
        result += f'M'
    else:
        result += '('
        getParenthesis(i, S[i][j])
        getParenthesis(1 + S[i][j], j)
        result += ')'


def getCorrectMultiplication(p: list):
    global S
    global result
    arrLength = len(p)
    # Create matrix
    M = [[0 for __ in range(arrLength)] for _ in range(arrLength)]
    S = [[0 for __ in range(arrLength)] for _ in range(arrLength)]

    for matrices in range(1, arrLength):
        for i in range(arrLength - matrices):
            j = i + matrices
            min = math.inf
            for k in range(i, j):
                item1 = M[i][k]
                item2 = M[k + 1][j]
                item3 = p[i-1]*p[k]*p[j]
                Q = item1 + item2 + item3
                # Redeclare min
                if(Q < min):
                    min = Q
                    S[i][j] = k

            M[i][j] = min

    # Parenthesis
    result = ''
    getParenthesis(1, arrLength - 1)
    # Split special cases
    result = result.replace('MM', "M x M")
    result = result.replace('M(', "M x (")
    result = result.replace(')M', ") x M")
    result = result.replace(')(', ") x (")
    
    # Build final
    final = ''
    resultArr = result.split('M')
    lastIndex = len(resultArr) - 1
    for i in range(len(resultArr)):
        if(i != lastIndex):
            final += f"{resultArr[i]}M{i + 1}"
        else:
            final += resultArr[i]

    print(final)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for arr in finalArr:
        getCorrectMultiplication(arr)


main()
