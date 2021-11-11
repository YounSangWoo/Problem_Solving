## 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

N = int(input())

pos = [0] * N
row = [False] * N
dia_1 = [False] * (N * 2 - 1)
dia_2 = [False] * (N * 2 - 1)
count = 0

def set_queen(c):
    for r in range(N):
        if(not row[r] and not dia_1[c + r] and not dia_2[c - r + (N-1)]):
            pos[c] = r
            if c == (N-1):
                global count
                count +=1
            else :
                row[r] = dia_1[c + r] = dia_2[c - r + (N-1)] = True
                set_queen(c + 1)
                row[r] = dia_1[c + r] = dia_2[c - r + (N-1)] = False
    return count

print(set_queen(0))
