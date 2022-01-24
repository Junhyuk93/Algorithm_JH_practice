n = input()
answer = 0

num = len(n)

for i in range(0,num-1):
    if n[i] != n[i+1]:
        answer += 1

answer = (answer+1)//2

print(answer)