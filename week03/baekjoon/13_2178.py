##### 문제 #####
# N×M크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 
# (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

##### 입력 #####
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
# 각각의 수들은 붙어서 입력으로 주어진다.

##### 출력 #####
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

import sys
from collections import deque

# N = row의 수, M = column의 수
N, M = map(int, sys.stdin.readline().split())

# 입력 값을 바탕으로 미로 리스트를 만든다.
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

# 방문 여부를 0과 1로 표시할 수 있는 리스트를 만든다.
visited = [[0] * M for _ in range(N)]

# BFS에 사용할 queue를 만든다.
queue = deque()
queue.append((0, 0))

# 시작 칸을 1로 바꾼다.
visited[0][0] = 1

# queue가 있는 동안 반복한다.
while queue:
    x, y = queue.popleft()

    # 시작 칸의 상, 하, 좌, 우를 모두 살핀다.
    for dir_x, dir_y in (-1, 0), (1, 0), (0, -1), (0, 1):
        new_x, new_y = x + dir_x, y + dir_y

        # 새로운 칸이 N행, M열보다 작고 0행, 0열보다 크거나 같다면
        if 0 <= new_x < N and 0 <= new_y < M:
            # 새로운 칸이 이동 가능한 곳인지, 그리고 방문했던 곳인지 확인한다.
            if maze[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                # 방문 표시를 해준다. 이때 이전까지 방문했던 곳의 정보들을 바탕으로 갱신한다.
                visited[new_x][new_y] = visited[x][y] + 1
                # 새로운 칸을 queue에 넣는다.
                queue.append((new_x, new_y))

    # 만약 마지막에 도착하면 지금까지 방문하면서 갱신해주었던 값을 출력한다.
    if x == N - 1 and y == M - 1:
        print(visited[x][y])
    

