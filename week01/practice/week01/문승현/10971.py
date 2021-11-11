## 문제
# 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
# N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 
# 다음 N개의 줄에는 비용 행렬이 주어진다. 
# 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. 
# W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

## 출력
# 첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

import sys
from itertools import combinations, permutations

# 도시의 갯수
N = int(input())
city_num = [i for i in range(N)]

# 각 도시에서 도시 이동할 때의 비용
cost_case = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def cost_cal(case):
    case_cost = 0
    for i in range(len(case)-1):
        if cost_case[case[i]][case[i+1]] != 0:
            case_cost += cost_case[case[i]][case[i+1]]
        else :
            return False
    if cost_case[case[-1]][case[0]] != 0:
        case_cost += cost_case[case[-1]][case[0]]
    else :
        return False
    return case_cost

min_cost = 1000000 * N
for case in permutations(city_num):
    print(case)
    case_cost = cost_cal(case)
    if case_cost:
        min_cost = min(min_cost, case_cost)

print(min_cost)
