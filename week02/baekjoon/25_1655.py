import sys, heapq

odd = []
even = []


count = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    count += 1
    if count % 2 != 0 :
        num = int(sys.stdin.readline().rstrip())
        heapq.heappush(odd, (-num, num))
    else :
        heapq.heappush(even, int(sys.stdin.readline().rstrip()))
    print(odd[0][1])

