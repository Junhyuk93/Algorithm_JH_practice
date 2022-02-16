import sys
n,m = map(int,input().split())

house_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
house_list.sort()


# 만족하는 거리중 최대값 찾기

def binary():
    start = 1
    end = max(house_list) - 1


    while start <= end:
        mid = (start+end)//2

        count = 1
        wifi = min(house_list)+mid # 1+4 = 5

        for i in range(1, len(house_list)):
            if wifi <= house_list[i]:
                count += 1
                wifi = house_list[i] + mid

        if count >= m:
            start = mid + 1
        elif count < m:
            end = mid - 1
    
    return print(end)

binary()