import  sys

N = int(input())
height_list = list(int(sys.stdin.readline()) for _ in range(N))
temp = height_list.pop()
result = [temp]


for _ in range(N-1):
    temp2 = height_list.pop()
    print(temp2)
    if temp >= temp2:
        pass
    else :
        temp = temp2
        result.append(temp)

print(len(result))