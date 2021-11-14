##### 문제 #####
# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 
# 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 여러 점이 같은 좌표를 가질 수도 있다.

##### 출력 ##### 
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.

import sys

N = int(input())

dot_list = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

def cal_distance(dot1, dot2):
    distance = (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2
    return distance

def dot_distance(start, end):
    if start == end:
        return float('inf')
        
    if end - start == 1:
        return cal_distance(dot_list[0], dot_list[1])
    
    mid = (start + end) // 2
    min_distance = min(dot_distance(start, mid), dot_distance(mid+1, end))
    
    possilbe_dot = []
    for i in range(start, end+1):
        if (dot_list[mid][0]-dot_list[i][0])**2 < min_distance:
            possilbe_dot.append(dot_list[i])
    
    possilbe_dot.sort(key=lambda x: x[1])

    p_len = len(possilbe_dot)
    for i in range(p_len-1):
        for j in range(i+1, p_len):
            if (possilbe_dot[i][1]-possilbe_dot[j][1]) ** 2 < min_distance:
                min_distance = min(min_distance, cal_distance(possilbe_dot[i], possilbe_dot[j]))
            else :
                break
    return min_distance

print(dot_distance(0, N-1))

