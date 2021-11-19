##### 문제 #####
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 같은 간선은 한 번만 주어진다.

##### 출력 #####
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
from collections import deque
sys.setrecursionlimit(10000)

# N = vertex의 수, M = edge의 수
N, M = map(int, sys.stdin.readline().split())

# vertex의 수를 고려하여 빈 리스트를 만들어 준다.
adj_graph = [[] for _ in range(N + 1)]
# print(adj_graph)

# vertex간의 관계를 표현하기 위해 adj_graph에 vertex를 index로 하여 값을 넣어준다.
for _ in range(M):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    adj_graph[vertex_1].append(vertex_2)
    adj_graph[vertex_2].append(vertex_1)

# vertex 방문 표시를 위한 리스트를 만든다.
visited = [False] * (N + 1)

def BFS(start_vertex):
    queue = deque()
    # queue를 하나 만들어주고, 시작 vertex를 넣어준다.
    queue.append(start_vertex)
    
    # queue가 존재하는 동안
    while queue:
        # queue에서 하나를 꺼내 방문 vertex 변수에 넣어주고
        visited_vertex = queue.popleft()
        # adj_graph에서 해당 vertex에 해당 하는 인덱스 값들을 확인한다.
        for vertex in adj_graph[visited_vertex]:
            # 해당 vertex를 방문하지 않았다면
            if visited[vertex] == False:
                # queue에 넣어주고
                queue.append(vertex)
                # 방문표시를 해준다.
                visited[vertex] = True

component = 0
# vetex의 수 만큼 반복한다.
for vertex in range(1, N + 1):
    # vetex를 방문하지 않았다면
    if visited[vertex] == False:
        # BFS 함수를 실행하고, componet를 1 증가 시켜준다.
        BFS(vertex)
        component += 1

print(component)



