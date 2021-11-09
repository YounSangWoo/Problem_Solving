numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]
    return numbers

print(selection_sort(numbers))

def selection_sort_using_min(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]
    return numbers
