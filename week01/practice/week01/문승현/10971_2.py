# import sys


# def dfs(current: int, cost):
#     global min_cost
#     if len(visited) == N and visit_cost[visited[-1]][0] != 0 :
#         # print(visited)
        
#         cost += visit_cost[visited[-1]][0]
#         min_cost = min(min_cost, cost)
#         return 

#     for next in range(1, N):
#         if visit_cost[current][next] != 0 and next not in visited:
#             visited.append(next)
#             dfs(next, cost+visit_cost[current][next])
#             visited.pop()


# #입력
# min_cost = float('inf')
# N = int(input())
# visit_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited = [0]
# # for i in range(N) :
# #     visited.append(N)
# #     dfs(N, 0)
# dfs(0, 0)
# print(min_cost)


import sys

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()


if __name__ == "__main__":

    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    # 각 번호에서 시작
    for i in range(N):
        dfs(i, i, 0, [i])

    print(min_value)