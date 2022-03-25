n = int(input())
m_list = list(map(int,input().split()))
m_list.sort()

print(m_list[(n-1)//2])