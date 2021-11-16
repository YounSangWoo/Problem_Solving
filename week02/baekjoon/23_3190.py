##### 문제 #####
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.


##### 입력 #####
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 
# 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며,
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.


##### 출력 #####
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
import sys
from collections import deque

board_size = int(input())
apples = int(input())

# 벽 : 1, 이동 가능 공간 : 0 
board = [[1] * (board_size + 2)] + [[1] + [0] * board_size + [1] for _ in range(board_size)] + [[1] * (board_size +2)]

# 사과 놓인 곳 : 2
for _ in range(apples):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 2

switching_num = int(input())
switching_info = deque(sys.stdin.readline().split() for _ in range(switching_num))

time_count = 0

# 현재 위치
start_x, start_y = 1, 1

# 이동 방향
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} ## 0:북 1:동 2:남 3:서

# 현재 방향 : 동(오른쪽)
current_dir = 1 

snake = deque([[1, 1]])

# 뱀의 위치 : 3
board[1][1] = 3

while True :
    start_x = start_x + direction[current_dir][0]
    start_y = start_y + direction[current_dir][1]

    if board[start_x][start_y] == 2 :
        board[start_x][start_y] = 3
        snake.append([start_x, start_y])
        time_count += 1
    
    elif board[start_x][start_y] == 0 :
        board[start_x][start_y] = 3
        snake.append([start_x, start_y])
        del_x, del_y = snake.popleft()
        board[del_x][del_y] = 0
        time_count += 1
    
    else :
        time_count += 1
        break
    
    if len(switching_info) != 0:
        if int(switching_info[0][0]) == time_count :
            if switching_info[0][1] == 'L':
                current_dir = (current_dir-1) % 4
            elif switching_info[0][1] == 'D':
                current_dir = (current_dir+1) % 4
            switching_info.popleft()
            
print(time_count)