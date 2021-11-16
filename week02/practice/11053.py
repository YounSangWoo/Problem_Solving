import sys
from bisect import bisect, bisect_left

N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

result = [0]

for num in numbers:
    if result[-1] < num :
        result.append(num)
    else :
        result[bisect_left(result, num)] = num

print(len(result)-1)