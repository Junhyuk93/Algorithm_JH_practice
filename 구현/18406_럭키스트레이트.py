n = list(map(int,input()))
point = (len(n) // 2)

l_n = n[:point]
r_n = n[point:]

if sum(l_n) == sum(r_n):
    print("LUCKY")
else:
    print("READY")