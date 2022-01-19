def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


# Memorization 기법
# 한번 계산도니 결과를 메모리제이션하기 위한 리스트 초기화
d = [0] * 100
# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo2(x):
    if x == 1 or x == 2:
        return 1
# 이미 한번 계산된 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
# 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

