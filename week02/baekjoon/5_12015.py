##### 문제 #####
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

##### 출력 #####
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

import sys
from bisect import bisect_left


N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
result = [0]

for num in numbers:
    if result[-1] < num:
        result.append(num)
    else :
        result[bisect_left(result, num)] = num
print(result)