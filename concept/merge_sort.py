numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def merge_sort(numbers):
    divide(numbers, 0 , len(numbers)-1)
    return numbers

def divide(numbers, left, right):
    if left == right :
        return
    else :
        mid = (left + right) // 2

        divide(numbers, left, mid)
        divide(numbers, mid+1, right)
        merge(numbers, left, mid, right)


def merge(numbers, left, mid, right) :
    
    sub_numbers1 = numbers[left:mid+1]
    sub_numbers2 = numbers[mid+1:right+1]

    pointer = left
    sub1_pointer = sub2_pointer = 0

    while sub1_pointer < len(sub_numbers1) and sub2_pointer < len(sub_numbers2):
        if sub_numbers1[sub1_pointer] <= sub_numbers2[sub2_pointer]:
            numbers[pointer] = sub_numbers1[sub1_pointer]
            sub1_pointer += 1
        else :
            numbers[pointer] = sub_numbers2[sub2_pointer]
            sub2_pointer += 1
        pointer += 1

    if sub1_pointer < len(sub_numbers1):
        numbers[pointer:right+1] = sub_numbers1[sub1_pointer:]
    elif sub2_pointer< len(sub_numbers2):
        numbers[pointer:right+1] = sub_numbers2[sub2_pointer:]

print(merge_sort(numbers))