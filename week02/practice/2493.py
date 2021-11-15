import sys

N = int(input())

top_height = list(map(int, sys.stdin.readline().split()))

stack = []
result = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_height[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    
    if not stack:
        result.append(0)
    
    stack.append([i, top_height[i]])

for i in result:
    print(i, end=" ")