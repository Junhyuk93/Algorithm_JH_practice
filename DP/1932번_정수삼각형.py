n = int(input())

triangle_list = []
dp = []
for i in range(1,n+1):
    triangle_list.append(list(map(int,input().split())))
    dp = [[0] * i for i in range(1,n+1)]
    dp[0][0] = triangle_list[0][0]

for j in range(1,n):
    for k in range(j+1):
        if k == 0:
            dp[j][k] = dp[j-1][k] + triangle_list[j][k]
        
        elif j == k:
            dp[j][k] = dp[j-1][k-1] + triangle_list[j][k]

        else:
            dp[j][k] = max(dp[j-1][k-1] + triangle_list[j][k], dp[j-1][k] + triangle_list[j][k])
print(max(dp[-1]))