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

while True :
    input = list(map(int, sys.stdin.readline().split()))
    if input[0] == 0 :
        break
    height_info = input[1:]

    width = 1
    area = 0

    def divide(height_info, area):    
        if len(height_info) == 1 :
            temp = height_info[0] * width
            area = max(temp, area)
            return area 
        elif not height_info :
            return area

        mid = len(height_info) // 2
        
        center = height_info[mid] * width
        temp = 0
        if (len(height_info) % 2) != 0 :
            if height_info[mid] < height_info[mid-1] and height_info[mid+1] :
                temp = height_info[mid] * 3
            elif height_info[mid-1] < height_info[mid] <= height_info[mid+1]:
                temp = height_info[mid] * 2
            elif height_info[mid-1] >= height_info[mid] > height_info[mid+1]:
                temp = height_info[mid] * 2
            elif height_info[mid-1]<= height_info[mid+1] < height_info[mid]:
                temp = height_info[mid+1] * 2
            elif height_info[mid+1]<= height_info[mid-1] < height_info[mid]:
                temp = height_info[mid-1] * 2
        
        if height_info[mid] == height_info[mid-1]:
            temp = len(height_info) * height_info[mid]

        center = max(center, temp)
        area = max(center, divide(height_info[:mid], area), divide(height_info[mid+1:], area))
        
        return area

    print(divide(height_info, 0))


    
    
    
    