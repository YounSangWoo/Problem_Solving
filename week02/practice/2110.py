import sys

houses, routers = map(int, sys.stdin.readline().split())

house_location = sorted(list(int(sys.stdin.readline()) for _ in range(houses)))

start = house_location[0]
end = house_location[-1]
max_distance = 0

while start <= end :
    mid = (start+end) // 2
    installed = house_location[0]
    count = 1
    for idx in range(1, len(house_location)):
        if house_location[idx] - installed >= mid :
            installed = house_location[idx]
            count += 1
    
    if count < routers :
        end = mid - 1
    else :
        start = mid + 1
        max_distance = max(max_distance, mid)

print(max_distance)

