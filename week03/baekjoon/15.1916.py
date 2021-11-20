##### 문제 #####
# N개의 도시가 있다. 
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
# 도시의 번호는 1부터 N까지이다.

##### 입력 #####
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 
# 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

##### 출력 #####
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

import sys, heapq

# 전체 도시의 수 
num_of_city = int(input())

# 도시들을 오가는 버스의 수 
num_of_bus = int(input())

# 도시의 수를 고려하여 graph를 만든다.
graph = [[] for _ in range(num_of_city + 1)]

# 최단 경로 테이블을 리스트로 만든다.
# 무한대 값은 int(1e9)로 설정해준다.
distance = [int(1e9)] * (num_of_city + 1)

# graph에 출발 도시와 도착 도시, 버스 비용을 표현해준다.
# 여기서는 리스트로 구현했다.
for _ in range(num_of_bus):
    start_city, end_city, fee = map(int,sys.stdin.readline().split())
    graph[start_city].append((end_city, fee))
# print(graph)

# 출발 도시와 도착 도시를 입력받는다.
start, end = map(int, sys.stdin.readline().split())


# 최단 비용을 찾는 함수다.
def DIJKSTRA(start):
    # queue를 하나 만들고, 힙으로 비용과 출발 도시를 넣어준다.
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        # 0, start
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

DIJKSTRA(start)
if distance[end] == 1000000:
    if end in graph[start]:
        print(graph[start][graph[start].index()][1])
else :
    print(distance[end])



