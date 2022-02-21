n = int(input())
dp = [False] * (1001)
dp[0] = True

for i in range(1, 1001):
    if i % 2 == 0:
        dp[i] = True
    if i % 3 == 0:
        dp[i] = True
    if i % 5 == 0:
        dp[i] = True

result = [i for i in range(len(dp)) if dp[i] is True]
print(result[n-1])