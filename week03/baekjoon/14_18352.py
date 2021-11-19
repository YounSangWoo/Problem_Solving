##### 문제 #####
# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 
# 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

##### 입력 #####
# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 
# 단, A와 B는 서로 다른 자연수이다.

##### 출력 #####
# X로부터 출발하여 도달할 수 있는 도시 중에서, 
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

import sys
from collections import deque

# N = 도시의 개수, M = 도로의 개수
# K = 거리 정보, X = 출발 도시 
N, M, K, X = map(int, sys.stdin.readline().split())

# 전체 도시의 수를 고려하여 adj_graph 리스트를 만들어준다.
adj_graph = [[] for _ in range(N+1)]

# 전체 도로의 수만큼 반복하면서
for _ in range(M):
    # 도시의 연결 여부를 adj_graph의 인덱스를 이용하여 표현한다.
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    adj_graph[vertex_1].append(vertex_2)

print(adj_graph)

# 방문 여부를 표시할 리스트를 만들어준다.
visited = [False] * (N + 1)

# 출발 도시에서 각 도시별 거리를 나타내는 리스트를 만들어준다.
distance = [0] * (N + 1)


def BFS(start):
    cities = []

    # queue를 하나 만들어주고, 출발 도시를 넣어준다.
    queue = deque()
    queue.append(start)
    
    # 출발 도시에 방문 표시를 해준다.
    visited[start] = True

    # 출발 도시에서 출발 도시까지의 거리는 0이다.
    distance[start] = 0

    # queue가 존재하는 동안
    while queue:
        # queue에서 하나를 꺼내 current_city 변수에 넣어준다.
        current_city = queue.popleft()

        # current_city의 인접 도시를 하나씩 살펴본다.
        for adj_city in adj_graph[current_city]:
            # 인접 도시를 방문하지 않았다면
            if not visited[adj_city]:
                # 인접 도시 방문 표시를 해주고 
                visited[adj_city] = True
                # queue에 넣어준다.
                queue.append(adj_city)
                # 거리도 표시해준다. 이때 거리는 출발 도시부터의 누적 거리다.
                distance[adj_city] = distance[current_city] + 1
                # 거리가 K라면 해당 도시를 cities에 넣어준다.
                if distance[adj_city] == K:
                    cities.append(adj_city)
                    
    if cities:
        cities.sort()
        for city in cities:
            print(city)
    else:
        print(-1)

BFS(X)