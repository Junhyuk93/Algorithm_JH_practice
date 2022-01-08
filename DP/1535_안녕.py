import itertools

n = int(input())

lost = [int(x) for x in input().split()]
get = [int(x) for x in input(). split()]

lost = [0] + lost
get = [0] + get

dp = [[0] * 101 for _ in range(n+1)]


for i in range(n+1):
    for j in range(100):
        if j < lost[i-1]:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lost[i-1]] + get[i-1])

print(dp[n][99])
