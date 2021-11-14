import sys
A, B, C = map(int, sys.stdin.readline().split())

def cal(A, B):
    if B == 1 :
        return A % C
    else :
        temp = cal(A, B // 2)
        if B % 2 == 0 :
            return temp * temp % C
        else :
            return temp * temp * A % C

print(cal(A,B))