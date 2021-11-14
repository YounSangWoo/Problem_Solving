##### 문제 #####
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.

##### 입력 #####
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

##### 출력 #####
# 요세푸스 순열을 출력한다.

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
numbers = deque()
for i in range(N) :
    numbers.append(i+1)

result = []
while len(result) < N :
    for _ in range(K-1) :
        output = numbers.popleft()
        numbers.append(output)
    result.append(numbers.popleft())

answer = '<'
for i in range(len(result)-1) :
    answer += f'{str(result[i])}, '
print(answer+str(result[-1]) +'>')
