##### 문제 #####
# 이진 트리를 입력받아 
# 전위 순회(preorder traversal), 
# 중위 순회(inorder traversal), 
# 후위 순회(postorder traversal) 
# 결과를 출력하는 프로그램을 작성하시오.

##### 입력 #####
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 
# 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

##### 출력 #####
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys

class Node :
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    
tree = {}

for _ in range(int(input())): 
    value, left, right  = list(sys.stdin.readline().split())
    tree[value] = Node(value, left, right)

# for i in tree :
#     print(f'tree_{i}의 left는 {tree[i].left}, right는 {tree[i].right} ')
    

def pre_order(node):
    print(node.value, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.value, end='')    
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.value, end='')    

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
