# ##### 문제 #####
# # 양의 정수 d와 n 개의 정수쌍, (hi, oi), 1 ≤ i ≤ n,이 주어져 있다. 
# # 여기서 hi와 oi는 사람 i의 집과 사무실의 위치이다. 
# # 길이 d의 모든 선분 L에 대하여, 집과 사무실의 위치가 모두 L에 포함되는 사람들의 최대 수를 구하는 프로그램을 작성하시오.

# ##### 입력 #####
# # 첫 번째 줄에 사람 수를 나타내는 양의 정수 n (1 ≤ n ≤ 100,000)이 주어진다. 
# # 다음 n개의 각 줄에 정수 쌍 (hi, oi)가 주어진다. 
# # 여기서 hi와 oi는 −100,000,000이상, 100,000,000이하의 서로 다른 정수이다. 
# # 마지막 줄에, 철로의 길이를 나타내는 정수 d (1 ≤ d ≤ 200,000,000)가 주어진다.

# ##### 출력 #####
# # 길이 d의 임의의 선분에 대하여, 집과 사무실 위치가 모두 그 선분에 포함되는 사람들의 최대 수를 한 줄에 출력한다. 

import sys, heapq

input = sys.stdin.readline
num_of_people = int(input())

location = [sorted(list(map(int, input().split()))) for i in range(num_of_people)]
location.sort(key=lambda x: x[1])
print(location)

distance = int(input())
print(f'distance = {distance}')
result = -1

heap = []
for s, e in location:

    if s + distance >= e :
        heapq.heappush(heap, s)

    while heap and heap[0] + distance <= e :
        heapq.heappop(heap)

    result = max(result, len(heap))
print(result)

