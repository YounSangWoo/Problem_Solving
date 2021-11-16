import sys

N, B = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def mul_matrix(size, matrix1, matrix2):
    board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                board[i][j] += matrix1[i][k] * matrix2[k][j]
            board[i][j] %= 1000
    return board

def divide(size, trial, matrix):
    if trial == 1:
        return matrix
    else :
        part = divide(size, trial//2, matrix)
        if trial % 2 == 0:
            return mul_matrix(size, part, part)
        else :
            return mul_matrix(size, mul_matrix(size, part, part), matrix)


result = divide(N, B, A)

for row in result :
    for num in row :
        print(num%1000, end=' ')
    print()