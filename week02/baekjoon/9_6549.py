##### 문제 #####
# 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 
# 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 
# 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

##### 입력 #####
# 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 
# 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 
# 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 
# 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

##### 출력 #####
# 각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

import sys

def divide(start_idx, end_idx):
    if start_idx == end_idx :
        return histogram_height[start_idx]
        
    else :
        # 중간 기준으로 살펴보기
        mid_idx = (start_idx + end_idx) // 2
        mid_left = mid_idx
        mid_right = mid_idx + 1
        mid_height = min(histogram_height[mid_left], histogram_height[mid_right])
        mid_area = 2 * mid_height

        width = 2
        while True:
            if (histogram_height[mid_left] == 0 or mid_left == start_idx) and (
                histogram_height[mid_right] == 0 or mid_right == end_idx):
                break
            elif histogram_height[mid_left] == 0 or mid_left == start_idx:
                if histogram_height[mid_right+1] < mid_height:
                    mid_height = histogram_height[mid_right+1]
                mid_right += 1
            elif histogram_height[mid_right] == 0 or mid_right == end_idx:
                if histogram_height[mid_left-1] < mid_height:
                    mid_height = histogram_height[mid_left-1]
                mid_left -= 1
            else :
                if histogram_height[mid_left-1] > histogram_height[mid_right+1]:
                    if histogram_height[mid_left-1] < mid_height:
                        mid_height = histogram_height[mid_left-1]
                    mid_left -= 1
                else :
                    if histogram_height[mid_right+1] < mid_height:
                        mid_height = histogram_height[mid_right+1]
                    mid_right += 1
            width += 1
            mid_area = max(mid_area, mid_height * width)

        return max(divide(start_idx, mid_idx), divide(mid_idx+1,end_idx), mid_area)


while True :
    histogram_info = list(map(int, sys.stdin.readline().split()))
    histogram_num = histogram_info[0]
    if histogram_num == 0 :
        break
    histogram_height = histogram_info[1:]
    print(divide(0, histogram_num-1))