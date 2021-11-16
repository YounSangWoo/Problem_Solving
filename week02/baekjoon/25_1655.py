##### 문제 #####
# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 
# 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
# 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

##### 입력 #####
# 첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. 
# N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
# 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 
# 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

##### 출력 #####
# 한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.


import sys, heapq

heap1 = []
heap2 = []

for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, (-num, num))
    else :
        heapq.heappush(heap2, (num, num))

    if heap2 and heap1[0][1] > heap2[0][1]:
        heap1_value = heapq.heappop(heap1)[1]
        heap2_value = heapq.heappop(heap2)[1]
        heapq.heappush(heap2, (heap1_value, heap1_value))
        heapq.heappush(heap1, (-heap2_value, heap2_value))
    
    print(heap1[0][1])


