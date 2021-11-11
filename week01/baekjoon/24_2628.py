## 문제
# 입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

## 입력
# 첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 
# 가로와 세로의 길이는 최대 100㎝이다. 
# 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 
# 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 
# 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 
# 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

## 출력
# 첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

width, height = map(int, input().split())
cutting = int(input())

width_list = [0, width]
height_list = [0, height]

for _ in range(cutting) :
    cut_di, cut_length = map(int, input().split())
    if cut_di == 0 :
        height_list.append(cut_length)
    else :
        width_list.append(cut_length)

width_list.sort()
height_list.sort()

area_list = []

for i in range(len(width_list)-1):
    for j in range(len(height_list)-1):
        w = width_list[i+1] - width_list[i]
        h = height_list[j+1] - height_list[j]
        area_list.append(w*h)

print(max(area_list))