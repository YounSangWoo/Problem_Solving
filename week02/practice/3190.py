import sys
from collections import deque

board_size = int(input())
num_of_apple = int(input())

# 벽 : 1
# 이동 가능 공간 : 0
# 사과 : 2
# 뱀 위치 : 3
board = [[1] * (board_size + 2)] + [[1] + [0] * board_size+ [1] for _ in range(board_size)] + [[1] * (board_size + 2)]

for _ in range(num_of_apple):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 2

board[1][1] = 3

for i in board:
    print(i)

# 뱀 이동 정보
num_of_switching = int(input())
switcing_info = deque(sys.stdin.readline().split() for _ in range(num_of_switching))

# 이동 방향
# 0 : 북, 1 : 동 
# 2 : 남, 3 : 서
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} 

# 현재 방향
cur_dir = 1

# 시작 정보
x, y = 1, 1
snake = deque([[1, 1]])
time_count = 0

while True:
    x, y = x + direction[cur_dir][0], y + direction[cur_dir][1]
    
    if board[x][y] == 2 :
        board[x][y] = 3
        snake.append([x, y])
        time_count += 1 
    
    elif board[x][y] == 0 :
        board[x][y] = 3
        snake.append([x, y])
        del_x, del_y = snake.popleft()
        board[del_x][del_y] = 0
        time_count += 1
    
    else :
        time_count += 1
        break
    
    if len(switcing_info) != 0:
        if int(switcing_info[0][0]) == time_count :
            if switcing_info[0][1] == 'L' :
                cur_dir = (cur_dir-1) % 4
            elif switcing_info[0][1] == 'D':
                cur_dir = (cur_dir+1) % 4
            switcing_info.popleft()

print(time_count)