##### 문제 #####
# 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 
# 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에는 전체 용액의 수 N이 입력된다. 
# N은 2 이상 100,000 이하이다. 
# 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 
# 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. 
# N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

##### 출력 #####
# 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 
# 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 
# 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.

import sys

N = int(input())
# print(f'용액의 수 : {N}')
liquid_list = sorted(list(map(int, sys.stdin.readline().split())))
# print(f'용액 리스트 : {liquid_list}')

to_zero = float('inf')
left_pointer = 0
right_pointer = N - 1
result = [0, 0]

while left_pointer < right_pointer:
    mix_liquid = liquid_list[left_pointer] + liquid_list[right_pointer]

    if abs(mix_liquid) < to_zero :
        to_zero = abs(mix_liquid)
        result[0], result[1] = liquid_list[left_pointer], liquid_list[right_pointer]
        
    if mix_liquid == 0 :
        result[0], result[1] = liquid_list[left_pointer], liquid_list[right_pointer]
        break
    else :
        if mix_liquid < 0 :
            left_pointer += 1
        else :
            right_pointer -= 1

print(f'{result[0]} {result[1]}')