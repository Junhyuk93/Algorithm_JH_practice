# 무지성 2중 for문 방법
# n, m = map(int,input().split())

# weight = list(map(int,input().split()))

# answer = 0

# for i in range(n):
#     for j in range(i,n):
#         if weight[i] != weight[j]:
#             answer += 1

# print(answer)


############################################


# 답지 해설
n, m = map(int,input().split())
weight = list(map(int,input().split()))

array = [0] * 11

for i in weight:
    array[i] += 1
    print(array)
result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    # 무게가 i 인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    n -= array[i]
    # B가 선택하는 경우의 수와 곱
    result += array[i] * n
    print(result)
print(result)

