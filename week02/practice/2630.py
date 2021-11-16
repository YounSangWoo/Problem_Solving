import sys

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(board)

color_list = []
def check_color(row, col, N):
    color = board[row][col]
    
    for r in range(row, row + N):
        for c in range(col, col + N):
            if color != board[r][c]:
                check_color(row, col, N // 2)
                check_color(row, col + N // 2, N // 2)
                check_color(row + N // 2, col, N // 2)
                check_color(row + N // 2, col + N // 2, N // 2)
                return

    if color == 0 :
        color_list.append(0)
    else :
        color_list.append(1)

check_color(0, 0, N)

print(color_list)