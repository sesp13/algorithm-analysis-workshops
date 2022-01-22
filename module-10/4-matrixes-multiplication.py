import math
S = []
result = ''

# ((M1 x M2) x M3)
# ['((', '(', '', '))((', '', ')', '))']


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
    resultArr = result.split('M')
    resultLength = len(resultArr) - 1
    final = ''
    for i in range(resultLength):
        nextIndex = i + 1
        current = resultArr[i]
        next = resultArr[nextIndex]
        if(current == ''):
            final += f'M{nextIndex}'
            nextIndex += 1
            if(next == '' or next[0] == '('):
                final += f'{current}M{nextIndex} x '
        else:
            if(next == '' or next[0] == '('):
                final += f'{current}M{nextIndex} x '
            else:
                final += current

    # Add last element
    # final += f" x M{resultLength}{resultArr[-1]}"

    print(final)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([int(x) for x in input().split()])

    for arr in finalArr:
        getCorrectMultiplication(arr)


main()
