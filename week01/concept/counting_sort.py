numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def counting_sort(numbers, max):
    n = len(numbers)
    f = [0] * (max + 1)
    b = [0] * n

    for i in range(n):
        f[numbers[i]] += 1
    
    for i in range(1, max + 1):
        f[i] += f[i - 1]

    for i in range(n - 1, -1, -1):
        f[numbers[i]] -= 1
        b[f[numbers[i]]] = numbers[i]
    
    for i in range(n):
        numbers[i] = b[i]
    
    return numbers

print(counting_sort(numbers,max(numbers)))