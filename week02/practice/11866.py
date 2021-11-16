from collections import deque
import  sys

N, K = map(int, sys.stdin.readline().split())

numbers = deque()

for i in range(N):
    numbers.append(i+1)

result = []

while N > len(result):
    for i in range(K-1):
        numbers.append(numbers.popleft())
    result.append(numbers.popleft())
print(result)
