numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        j = i
        temp = numbers[i]
        while j > 0 and numbers[j - 1] > temp:
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = temp

    return numbers

print(insertion_sort(numbers))