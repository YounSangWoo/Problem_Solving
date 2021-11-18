##### 문제 ##### 
# 이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.
# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

##### 입력 #####
# 트리를 전위 순회한 결과가 주어진다. 
# 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 
# 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 
# 같은 키를 가지는 노드는 없다.

##### 출력 #####
# 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.


import sys
sys.setrecursionlimit(100000)

# pre_order 결과를 일단 만든다.
pre_order = []
while True:
    try :
        pre_order.append(int(sys.stdin.readline().rstrip()))
    except:
        break


def get_post_order(pre_order):
    length = len(pre_order)

    # 들어온 값이 1개 미만이라면 그냥 그 값을 반환한다.
    if length <= 1:
        return pre_order
    
    # pre_order에 root 다음 숫자부터, root와 비교한다.
    for i in range(1, length):
        # root보다 큰 수를 기준으로 다시 함수를 호출한다.
        if pre_order[i] > pre_order[0]:
            # root보다 큰 수 전까지, 큰 수 부터 끝까지, root
            return get_post_order(pre_order[1:i]) + get_post_order(pre_order[i:]) + [pre_order[0]]
    
    return get_post_order(pre_order[1:]) + [pre_order[0]]


result = get_post_order(pre_order)
for num in result :
    print(num)


