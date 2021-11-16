import  sys

N = int(input())

liquid_list = sorted(list(map(int, sys.stdin.readline().split())))


to_zero = float('inf')
left_pointer = 0
right_pointer = N - 1
result = [0, 0]

while left_pointer < right_pointer :
    mix_liquid = abs(liquid_list[left_pointer] + liquid_list[right_pointer])

    if mix_liquid < to_zero:
        to_zero = mix_liquid
        result[0], result[1] = liquid_list[left_pointer], liquid_list[right_pointer]
    
    if mix_liquid == 0 :
        result[0], result[1] = liquid_list[left_pointer], liquid_list[right_pointer]
    else :
        if mix_liquid < 0 :
            left_pointer += 1
        else :
            right_pointer -= 1

print(result)