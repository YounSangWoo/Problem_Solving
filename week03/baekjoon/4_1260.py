##### 문제 #####
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

##### 입력 #####
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

##### 출력 #####
# 첫째 줄에 DFS를 수행한 결과를, 
# 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

import sys
from collections import deque

# N = vertex의 수, M = edge의 수, V = 시작 vertex
N, M, V = map(int, sys.stdin.readline().split())

# 인접 행렬을 통해서 vertex와 vertex 사이의 관계를 나타낸다.
# vertex가 연결되어 있으면 True 아니면 False이다.
graph_DFS = [[0] * (N + 1) for _ in range(N + 1)]
graph_BFS = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    graph_DFS[vertex_1][vertex_2] = graph_DFS[vertex_2][vertex_1] = True
    graph_BFS[vertex_1][vertex_2] = graph_BFS[vertex_2][vertex_1] = True

# 방문 여부를 True or False로 표시한다.
visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)

def DFS(start_vertex):
    # 시작 vertex 방문 여부를 True로 바꾼다.
    visited_DFS[start_vertex] = True
    print(start_vertex, end=' ')

    # vertex의 수 만큼 반복하면서 방문 여부를 확인한다.
    for vertex in range(1, N + 1):
        # 시작 vertex와 연결되어 있고, 아직 방문하지 않은 vertex라면
        if graph_DFS[start_vertex][vertex] == True and visited_DFS[vertex] == False:
            # 해당 vertex를 다시 DFS 한다.
            DFS(vertex)


def BFS(start_vertex):
    # queue를 하나 만들어주고, 해당 queue에 start_vertex를 넣어준다.
    queue = deque()
    queue.append(start_vertex)
    
    # 시작 vertex 방문 여부를 True로 바꾼다.
    visited_BFS[start_vertex] = True

    # queue가 존재하는 동안 반복한다.
    while queue:
        # queue에서 방문한 vertex를 꺼낸다.
        visited_vertex = queue.popleft()
        print(visited_vertex, end=' ')
        # vertex의 수 만큼 반복하면서 방문 여부를 확인한다.
        for vertex in range(1, N + 1):
            # 시작 vertex와 연결되어 있고, 아직 방문하지 않은 vertex라면
            if graph_BFS[visited_vertex][vertex] == True and visited_BFS[vertex] == False:
                # queue에 넣어주고, 방문 표시를 해준다.
                queue.append(vertex)
                visited_BFS[vertex] = True

DFS(V)
print()
BFS(V)