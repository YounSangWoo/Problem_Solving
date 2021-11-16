##### 문제 #####
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.


##### 입력 #####
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 
# 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 
# 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.


##### 출력 #####
# 첫째 줄에 최소 비교 횟수를 출력한다.

import sys, heapq

N = int(input())

cards = []

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

if len(cards) == 1:
    print(0)
else :
    count = 0
    while len(cards) > 1:
        temp_1 = heapq.heappop(cards)
        temp_2 = heapq.heappop(cards)
        count += temp_1 + temp_2
        heapq.heappush(cards, temp_1 + temp_2)
    
    print(count)