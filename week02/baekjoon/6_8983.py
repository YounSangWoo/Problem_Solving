##### 문제 #####
# 사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

##### 입력 #####
# 입력의 첫 줄에는 사대의 수 M (1 ≤ M ≤ 100,000), 
# 동물의 수 N (1 ≤ N ≤ 100,000), 
# 사정거리 L (1 ≤ L ≤ 1,000,000,000)이 빈칸을 사이에 두고 주어진다.
# 두 번째 줄에는 사대의 위치를 나타내는 M개의 x-좌표 값이 빈칸을 사이에 두고 양의 정수로 주어진다. 
# 이후 N개의 각 줄에는 각 동물의 사는 위치를 나타내는 좌표 값이 x-좌표 값, y-좌표 값의 순서로 빈칸을 사이에 두고 양의 정수로 주어진다. 
# 사대의 위치가 겹치는 경우는 없으며, 동물들의 위치가 겹치는 경우도 없다. 
# 모든 좌표 값은 1,000,000,000보다 작거나 같은 양의 정수이다. 

##### 출력 #####
# 출력은 단 한 줄이며, 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력한다.

import sys
from bisect import bisect_left

total_rifles, total_animals, lenghts = map(int, sys.stdin.readline().split())
rifles_loc = sorted(list(map(int, sys.stdin.readline().split())))
animals_loc = [list(map(int, sys.stdin.readline().split())) for _ in range(total_animals)]
catch_count = 0

def find_closest_rifle(rifles_loc, x):
    rifles_idx = bisect_left(rifles_loc, x)
    if rifles_loc == 0:
        return rifles_loc[0]
    elif rifles_idx == len(rifles_loc):
        return rifles_loc[-1]
    else :
        return rifles_loc[rifles_idx]

for x, y in animals_loc :
    closest_rifle = find_closest_rifle(rifles_loc, x)
    if abs(closest_rifle - x) + y <= lenghts:
        catch_count += 1

print(catch_count)
