## 문제
# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 
# 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에 정수 N, r, c가 주어진다.

## 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

# N, r, c = map(int, input().split())
# visit_count = 0

# while N > 1 :
#     total_size = (2 ** N)
#     target_size = total_size // 2

#     if r < target_size and c < target_size :
#         pass
#     elif r < target_size and c >= target_size :
#         visit_count += target_size ** 2 * 1
#         c -= target_size
#     elif r >= target_size and c < target_size :
#         visit_count += target_size ** 2 * 2
#         r -= target_size
#     elif r >= target_size and c >= target_size :
#         visit_count += target_size ** 2 * 3
#         c -= target_size
#         r -= target_size

#     N -= 1

# if r == 0 and c == 0 :
#     print(visit_count)
# elif r ==0 and c == 1:
#     print(visit_count + 1)
# elif r == 1 and c == 0:
#     print(visit_count + 2)
# elif r == 1 and c == 1:
#     print(visit_count + 3)



# N, r, c = map(int, input().split())
# 2 3 1

N, r, c = 3, 7, 7
visit_count = 0

while N > 1 :
    total_size = 2 ** N
    target_size = total_size // 2

    if r < target_size and c < target_size:
        pass
    elif r < target_size and c >= target_size:
        visit_count += target_size ** 2 * 1
        c -= target_size
    elif r > target_size and c < target_size:
        visit_count += target_size ** 2 * 2
        r -= target_size
    elif r >= target_size and c >=target_size:
        visit_count += target_size ** 2 * 3
        r -= target_size
        c -= target_size
    N -= 1

if r == 0 and c == 0:
    print(visit_count)
elif r == 0 and c == 1:
    print(visit_count+1)
elif r == 1 and c == 0:
    print(visit_count+2)
else :
    print(visit_count+3)