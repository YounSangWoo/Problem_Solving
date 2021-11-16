import sys

N = int(sys.stdin.readline())

top_height = list(map(int, sys.stdin.readline().split()))

stack = [top_height[-1]]
result = [0] * N

for i in reversed(range(N-1)):
    while stack:
        if stack[-1] < top_height[i]:
            temp = top_height.index(stack[-1])
            result[temp] = i + 1
            stack.pop()
        else :
            break
    stack.append(top_height[i])

print(result)

