## 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 
# 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

## 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

import sys
from itertools import permutations

# 정수의 갯수 
N = int(input())

# N개의 정수를 담고 있는 리스트 만들기
numbers = list(map(int, sys.stdin.readline().split()))

# 해당 리스트를 이용하여 가능한 경우의 수 구하기
case_list = list(permutations(numbers, N))

result = 0
for i in range(len(case_list)):
    max_sum = 0
    for j in range(N - 1):
        max_sum += abs(case_list[i][j] - case_list[i][j+1])
    result = max(result, max_sum)

print(result)