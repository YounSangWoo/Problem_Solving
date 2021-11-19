##### 문제 #####
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 
# 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에는 컴퓨터의 수가 주어진다. 
# 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

##### 출력 #####
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

import sys
from collections import deque
sys.setrecursionlimit(10000)

# 전체 컴퓨터의 수
num_of_computer = int(sys.stdin.readline().rstrip())

# 컴퓨터들을 연결하는 edge의 수
num_of_edge = int(sys.stdin.readline().rstrip())

# 전체 컴퓨터의 수를 고려하여 adj_graph 리스트를 만들어준다.
adj_graph = [[] for _ in range(num_of_computer + 1)]

# 전체 edge의 수만큼 반복하면서
for _ in range(num_of_edge):
    # 컴퓨터들의 연결 여부를 adj_graph의 인덱스를 이용하여 표현한다.
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())
    adj_graph[vertex_1].append(vertex_2)
    adj_graph[vertex_2].append(vertex_1)

# 방문 여부를 표시할 리스트를 만들어준다.
visited = [False] * (num_of_computer + 1)

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

BFS(1)
print(sum(visited)-1)