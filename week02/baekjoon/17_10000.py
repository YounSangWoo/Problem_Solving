##### 문제 #####
# x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.
# 원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.
# 영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.

##### 입력 #####
# 첫째 줄에 원의 개수 N(1 ≤ N ≤ 300,000)이 주어진다.
# 다음 N개 줄에는 각 원의 정보 xi와 ri가 정수로 주어진다. 
# xi는 원의 중심 좌표이며, ri는 반지름이다. (-109 ≤ xi ≤ 109, 1 ≤ ri ≤ 109)
# 입력으로 주어지는 원은 항상 유일하다.

##### 출력 #####
# 첫째 줄에 원으로 인해서 만들어지는 영역의 개수를 출력한다.

import sys 
from bisect import bisect_left
sys.setrecursionlimit(100000)


circle_num = int(input())
circle_info = []
for i in range(circle_num):
    x, r = map(int, sys.stdin.readline().split())
    circle_info.append((x-r, x+r))

# circle_info를 x는 오름차순, y는 내림차순으로 정렬
circle_info.sort(key= lambda x:(x[0], -x[1]))

k = 0
def solve(u, v):
    global k 
    if circle_info[u][1] == circle_info[v][1]:
        k += 1
        return
    pos = bisect_left(circle_info, (circle_info[v][1], -2e9))
    if pos == len(circle_info):
        return
    if circle_info[pos][0] == circle_info[v][1]:
        solve(u, pos)

for i in range(circle_num-1):
    if circle_info[i][0] == circle_info[i+1][0]:
        solve(i, i+1)

print(circle_num + 1 + k)