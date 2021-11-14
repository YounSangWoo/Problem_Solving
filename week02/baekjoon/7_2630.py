##### 문제 #####
# 입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. 
# N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 
# 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

##### 출력 #####
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

import sys

N = int(input())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
color_list = []

def divide(row, col, N):
    color = square[row][col]
    for i in range(row, row+N):
        for j in range(col, col+N):
            if color != square[i][j]:
                # 1사분면
                divide(row, col, N//2)
                # 2사분면
                divide(row, col + N//2, N//2)
                # 3사분면
                divide(row + N//2, col, N//2)
                # 4사분면
                divide(row + N//2, col + N//2, N//2)
                return
    
    if color == 0 :
        color_list.append(0)
    else :
        color_list.append(1)


divide(0, 0, N)
print(color_list.count(0))
print(color_list.count(1))