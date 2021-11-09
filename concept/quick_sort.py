numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]


def quick_sort(numbers, left, right):
    left_pointer = left
    right_pointer = right
    pivot = numbers[(left+right) // 2]

    while left_pointer <= right_pointer:
        while numbers[left_pointer] < pivot:
            left_pointer += 1
        while numbers[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer <= right_pointer:
            numbers[left_pointer], numbers[right_pointer] = numbers[right_pointer], numbers[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    if left < left_pointer:
        quick_sort(numbers, left, right_pointer)
    if right_pointer < right:
        quick_sort(numbers, left_pointer, right)

    return numbers


print(quick_sort(numbers, 0, len(numbers)-1))
