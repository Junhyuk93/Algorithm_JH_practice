n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 종료
    if x <= -1 or x>= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1

        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)