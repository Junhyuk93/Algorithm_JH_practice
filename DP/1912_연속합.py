n = int(input())

num_list = list(map(int,input().split()))

dp = [0] * len(num_list)
dp[0] = num_list[0]

# dp 배열을 만들고, 기존 값과 비교하여 이전 값이 더 클경우, max 값을 통해 dp 배열에 입력

for i in range(len(num_list)):
    dp[i] = max(num_list[i], dp[i-1] + num_list[i])

print(max(dp))
