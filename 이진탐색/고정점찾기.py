import sys

n = int(input())
array = list(map(int, input().split()))
start = 0
end = n-1


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return '-1'


res = binary_search(array, start, end)
print(res)