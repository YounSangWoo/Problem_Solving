import sys
from bisect import bisect_left

rifles, animals, lenghts = map(int, sys.stdin.readline().split())
rifles_loc = sorted(list(map(int, sys.stdin.readline().split())))
animals_loc = [list(map(int, sys.stdin.readline().split())) for _ in range(animals)]

def find_closest_rifle(rifles_loc, x):
    rifles_idx = bisect_left(rifles_loc, x)

    if rifles_idx == 0 :
        return rifles_loc[0]
    elif rifles_idx == len(rifles_loc):
        return rifles_loc[-1]
    else :
        left = rifles_loc[rifles_idx-1]
        right = rifles_loc[rifles_idx]

        if 2 * x < left + right :
            return left
        else :
            return right


catch_count = 0
for x, y in animals_loc:
    closest_rifle = find_closest_rifle(rifles_loc, x)
    if abs(closest_rifle-x) + y <= lenghts:
        catch_count += 1

print(catch_count)
