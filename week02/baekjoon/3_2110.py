##### 문제 ##### 
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

##### 입력 ##### 
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

##### 출력 ##### 
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

import sys

house_num, router_num = map(int, sys.stdin.readline().split())
# print(f'집의 개수 : {house_num}, 공유기 개수 : {router_num}')

house_loc = sorted([int(sys.stdin.readline()) for _ in range(house_num)])
# print(f'집의 좌표 : {house_loc}')

first_house_loc = 1
last_house_loc = house_loc[-1]

max_distance = 0
while last_house_loc >= first_house_loc:
    center_house_loc = (first_house_loc + last_house_loc) // 2
    router_count = 1

    installed = house_loc[0]
    for i in range(1, house_num):
        if house_loc[i] >= installed + center_house_loc:
            router_count += 1
            installed = house_loc[i]
    
    if router_count < router_num :
        last_house_loc = center_house_loc - 1
    else :
        first_house_loc = center_house_loc + 1
        max_distance = center_house_loc

print(max_distance)