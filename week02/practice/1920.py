N = int(input())
N_list= sorted(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))

def binary_search(target, N_list, left, right):
    if left > right :
        return 0
    
    mid = (left + right) // 2 

    if target == N_list[mid]:
        return 1
    elif target < N_list[mid]:
        return binary_search(target, N_list, left, mid-1)
    else :
        return binary_search(target, N_list, mid+1, right)


for target in M_list :
    print(binary_search(target, N_list, 0, N-1))