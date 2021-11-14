##### 문제 #####
# 크기가 N*N인 행렬 A가 주어진다. 
# 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
# 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

##### 입력 #####
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

##### 출력#####
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

import sys

N, B = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def matrix_mul(size, matrix1, matrix2):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result

def divide(size, trial, matrix):
    if trial == 1:
        return matrix
    else :
        part = divide(size, trial//2, matrix)
        if trial % 2 == 0 :
            return matrix_mul(size, part, part)
        else :
            return matrix_mul(size, matrix_mul(size, part, part), matrix)

result = divide(N, B, A)
for row in result :
    for num in row :
        print(num%1000, end=' ')
    print()