from itertools import combinations

n = int(input())

money_list = list(map(int, input().split()))

money_list.sort()

answer = 1

for i in money_list:
    # print(i)
    if answer < i:
        break
    
    answer += i
    # print(answer)
print(answer)