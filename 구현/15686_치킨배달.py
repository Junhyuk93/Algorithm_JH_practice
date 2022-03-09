import itertools
import sys


n,m = map(int,(input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

c = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            c.append([i,j])
            arr[i][j] = 0

# 치킨집 위치중 m개 고르기            
result = list(itertools.combinations(c,m))
# print(result)
min_distance = 9999999

for i in range(len(result)):
    distance = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                temp = min_distance
                for j in range(m):
                    temp = min(temp, abs(x - result[i][j][0]) + abs(y - result[i][j][1]))
                distance += temp

    min_distance = min(min_distance, distance)

print(min_distance)