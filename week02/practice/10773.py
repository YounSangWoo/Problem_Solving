import sys

K = int(input())

stack = []
for _ in range(K):
    order = int(sys.stdin.readline())
    if order == 0 :
        stack.pop()
    else :
        stack.append(order)

print(sum(stack))