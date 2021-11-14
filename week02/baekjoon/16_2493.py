##### 문제 #####

##### 입력 #####
# 첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. 
# N은 1 이상 500,000 이하이다. 
# 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 
# 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.

##### 출력 #####
# 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 
# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.

import sys

N = int(input())
top_list = list(map(int, sys.stdin.readline().split()))
stack = [top_list[-1]]
result = [0]* N

for i in reversed(range(N-1)):
    while stack :
        if top_list[i] > stack[-1] :
            index = top_list.index(stack[-1])
            result[index] = i+1
            stack.pop()
        else :
            break
    stack.append(top_list[i])

for i in result:
    print(i, end = " ")
