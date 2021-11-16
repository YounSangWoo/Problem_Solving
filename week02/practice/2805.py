import sys

num_of_tree, wishing_length = map(int, sys.stdin.readline().split())

tree_heights = list(map(int, sys.stdin.readline().split()))

ground = 0

highest_tree = max(tree_heights)

while ground <= highest_tree:

    cutting_heihgt = (ground + highest_tree) // 2

    total_length = 0

    for tree in tree_heights:

        if tree > cutting_heihgt:

            total_length += tree - cutting_heihgt
        
    if total_length >= wishing_length:
        
        ground = cutting_heihgt + 1
    
    else :
    
        highest_tree = cutting_heihgt -1

print(highest_tree)    
