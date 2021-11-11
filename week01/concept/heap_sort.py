import heapq
numbers = [3, 8, 5, 0, 11, 4, 7, 13, 1, 2]

def heap_sort(numbers) :
    heap = []
    for i in numbers :
        heapq.heappush(heap, i)
    for i in range(len(numbers)):
        numbers[i] = heapq.heappop(heap)
    return numbers

print(heap_sort(numbers))