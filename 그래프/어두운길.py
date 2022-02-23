import sys

# n은 도시, m은 도로 수
n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 간선 정보 담을 리스트
edges = []
total_cost = 0
for _ in range(m):
    x, y, cost = map(int, input().split())  # x -> y, cost
    total_cost += cost
    edges.append((cost, x, y))
edges.sort()

# 간선 정보 하나씩 처리
result = 0
for i in range(m):
    cost, x, y = edges[i]
    # find 연산 후 부모 노드 같지 X = 사이클 발생 X = union연산 후 최소신장에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        result += cost
        union_parent(parent, x, y)

print(total_cost - result)