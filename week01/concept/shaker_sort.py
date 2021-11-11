numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def shaker_sort(numbers):
    left = 0
    right = len(numbers) - 1
    last = right 
    while left < right:
        for i in range(right, left, -1):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                last = i
        left = last
        
        for i in range(left, right):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                last = i
        right = last
    return numbers

