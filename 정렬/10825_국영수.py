n = int(input())

score = []
for _ in range(n):
    name, x, y, z = input().split()
    score.append((name, int(x), int(y), int(z)))
score.sort(key=lambda i: i[0])
score.sort(key=lambda i: i[3], reverse=True)
score.sort(key=lambda i: i[2])
score.sort(key=lambda i: i[1], reverse=True)

for i in score:
    print(i[0])