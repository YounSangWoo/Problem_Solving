numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1) :
        for j in range(n-1, i, -1) :
            if  numbers[j-1] > numbers[j] :
                numbers[j-1], numbers[j]  = numbers[j], numbers[j-1]
    return numbers
