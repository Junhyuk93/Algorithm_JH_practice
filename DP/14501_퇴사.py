n = int(input())

time_list = []
money_list = []

dp = [0 for i in range(n+1)]

for i in range(n):
    x, y = map(int,input().split())
    time_list.append(x)
    money_list.append(y)

# for j in range(n):
    # if time_list[j] + 
# N부터 시작할 경우 너무 복잡해짐

# 역순으로 진행하면 고려하지않아도 될듯?
for j in range(n-1, -1, -1):
    # 또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
    if time_list[j] + j > n:
        dp[j] = dp[j+1]
    
    # 상담을 받는다 했을 때 돈 + 이 다음 예상되는 돈 vs 상담을 안받았을때의 돈
    else:
        dp[j] = max(money_list[j] + dp[j + time_list[j]], dp[j+1])
    print(dp)
print(dp[0])