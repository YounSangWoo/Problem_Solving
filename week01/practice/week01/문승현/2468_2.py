import sys
sys.setrecursionlimit(100000)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, rain):
    need_visited= []
    need_visited.append((x,y))
    while need_visited:
        root = need_visited.pop()
        # print(f' root변수값 : {root}')
        # print(f'visited리스트에 있나 없나 {visited[root[0]][root[1]]}')
        if visited[root[0]][root[1]] == False:
            visited[root[0]][root[1]] = True
            for i in range(4):
                nx = root[0] + dx[i]
                ny = root[1] + dy[i]
                #0,0  1,1  2,0  1,-1
                if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and (heights[nx][ny] > rain):
                    print(f'옆집 탐색 {(nx, ny)}')
                    need_visited.append((nx,ny))
                    print(f'남은 집은 : {need_visited}')



n = int(sys.stdin.readline())
heights = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, heights))
min_height = min(map(min, heights))
ans = 1
for rain in range(min_height, max_height):
    print(f'내리는 비의 양은: {rain}')
    visited = [[False]*n for i in range(n)]
    safe = 0
    for r in range(n):
        for c in range(n):
            print(f' r: {r}, c: {c}. visited[r][c] : {visited[r][c]}, heights[r][c] : {heights[r][c]>rain}')
            if not visited[r][c] and heights[r][c] > rain:
                safe += 1
                print(f'safe는 {safe}')
                DFS(r, c, rain)
    ans= max(ans, safe)
print(ans)