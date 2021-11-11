##### 문제 #####
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
# 둘째 줄에는 나무의 높이가 주어진다. 
# 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 
# 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

##### 출력 #####
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

import sys

num_tree, target_length  = map(int, sys.stdin.readline().split())
tree_height = list(map(int, sys.stdin.readline().split()))

ground = 0
highest_height = max(tree_height)

while ground <= highest_height :
    new_hightes_height = (ground + highest_height) // 2

    total_lenght = 0
    for height in tree_height:
        if height >= new_hightes_height :
            total_lenght += height - new_hightes_height
            
    if total_lenght >= target_length:
        ground = new_hightes_height + 1
    else :
        highest_height = new_hightes_height -1
        
        
print(highest_height)