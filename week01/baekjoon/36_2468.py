## 문제
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
# N은 2 이상 100 이하의 정수이다.
# 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다.
# 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
# 높이는 1이상 100 이하의 정수이다.

## 출력
# 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

import sys
sys.setrecursionlimit(100000)

N = int(input())
height_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def adj_area(x, y, height):
    visited_area[x][y] = True
    for dir_x, dir_y in (-1, 0), (1, 0), (0, -1), (0, 1) :
        new_x, new_y = x + dir_x, y + dir_y
        if 0 <= new_x < N and 0 <= new_y < N and not visited_area[new_x][new_y] and height_info[new_x][new_y] > height:
            adj_area(new_x, new_y, height)

result = 0
for height in range(min(min(height_info)), max(max(height_info))):
    visited_area = [[False] * N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if not visited_area[i][j] and height_info[i][j] > height:
                safe_area += 1
                adj_area(i, j, height)
    result = max(result, safe_area)

print(result)