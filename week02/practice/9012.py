import sys

T = int(input())

def check(data):
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        else :
            if stack:
                stack.pop()
            else :
                return False
    
    if not stack :
        return True
    else :
        return False

for _ in range(T) :
    data = sys.stdin.readline().rstrip()
    if check(data):
        print('YES')
    else :
        print('NO')
