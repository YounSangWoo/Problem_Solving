# Spanning Tree란 그래프 내의 모든 정점을 포함하는 트리로써 그래프의 최소 연결 부분 그래프이다.
# n 개의 정점을 가지는 그래프의 최소 연결 간선의 개수는 n - 1 개이다.
# 그 중 Minimum Spanning Tree란 그래프의 간선이 가중치를 가지고 있을 때,
# Spanning Tree 중 그 가중치의 합이 가장 작은 트리를 의미한다.

##### 문제 #####
# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

##### 입력 #####
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

##### 출력 #####
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.


# vertex가 속하는 group을 찾아주는 함수
def find_group(vertex):
    # vertex가 속하는 그룹이 초기 값과 다르다면 해당 그룹을 찾아서 리턴한다.
    if group[vertex] != vertex:
        group[vertex] = find_group(group[vertex])
    return group[vertex]

# vertex의 group을 찾아서 그 값을 비교하여 하나로 합치는 함수
def union_group(vertex_1, vertex_2):
    vertex_1 = find_group(vertex_1)
    vertex_2 = find_group(vertex_2)
    # 부등호의 방향은 사실 의미없다.
    # 서로 다른 group이란 것이 확인이 되면 어떤 vertex를 기준으로 하던 
    # 하나의 group으로 만들어주는 것이 중요하다.
    if vertex_1 < vertex_2:
        group[vertex_2] = vertex_1
    else:
        group[vertex_1] = vertex_2


vertex, edge = map(int, input().split())

# vertex 수 만큼 group 리스트를 만든다.
# 초기에는 각각의 vertex들이 서로 다른 그룹(1, 2, 3)에 속한다.
group = [i for i in range(vertex + 1)]
print(group)

edges = []
result = 0

# edge 별로 연결하는 vertex와 weight를 리스트로 만든다.
# 이때, weight를 0번째 인덱스 자리로 순서를 바꾸어 입력하였는데
# 이는 weight 순으로 정렬을 편하게 하기 위함이니 원래대로 입력하고 정렬을 다르게 구현해도 된다.
for _ in range(edge):
    vertex_1, vertex_2, weight = map(int, input().split())
    edges.append((weight, vertex_1, vertex_2))

# weight를 오름차순으로 정렬한다.
edges.sort()
print(edges)

# edge들을 담은 리스트에서 하나씩 edge를 꺼낸다.
for edge in edges:
    weight, vertex_1, vertex_2 = edge
    print(vertex_1, vertex_2)

    # vertex의 그룹이 다를 경우, 두 vertex를 연결하여 하나의 group으로 만들어준다.
    if find_group(vertex_1) != find_group(vertex_2):
        union_group(vertex_1, vertex_2)

        # vertex를 연결하였다면, 해당 weight를 result에 더해준다.
        result += weight

print(result)
