from collections import deque
# 1. 그래프를 입력받는다. 일반적으로 탐색 문제에서는 '1 2'라는 입력이 들어오면 graph[1]에 2를 넣고, graph[2]에는 1을 넣어서 양방향으로 연결된 관계를 표현해준다 

# 그러나 이 문제에서는 최단 거리를 구하기 때문에 양방향 관계가 필요가 없다. 왔던 곳으로 되돌아간다면 최단 거리가 될 수 없기 때문이다 

# 2. bfs로 탐색해준다 

#     1. 속도 향상을 위해 큐를 deque로 구현해준다 

#     2. 큐에 시작점인 x를 넣고 

#     3. 큐에서 팝한 요소를 now로 선언 

#     4. now에 연결된 도시 nxt에 대해 

#         1. 아직 방문하지 않은 도시라면 지금까지의 거리(answer[now])에 1을 더한 값을 answer[nxt]로 저장해준다 

#         2. nxt를 큐에 append하여 다음 탐색할 곳으로 지정해준다 
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

answer = [-1] * (n+1)

answer[x] = 0
for _ in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)

que = deque([x])

while que:
    now  = que.popleft()
    for nxt in graph[now]:
        if answer[nxt] == -1:
            answer[nxt] = answer[now] + 1
            que.append(nxt)
for i in range(n+1):
    if answer[i] == k:
        print(i)

if k not in answer:
    print(-1)