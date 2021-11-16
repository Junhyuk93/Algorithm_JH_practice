import sys

# answer의 길이가 M과 같아지면 출력

N,M = map(int,sys.stdin.readline().split())

answer = []

def dfs(start):
    if len(answer) == M:   
        print(' '.join(map(str,answer)))
        return

    for i in range(start,N+1): 
        answer.append(i) 
        dfs(i)
        answer.pop()

dfs(1)