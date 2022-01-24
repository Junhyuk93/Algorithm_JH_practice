def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = i #첫행 초기화
    for j in range(1, m + 1):
        dp[0][j] = j #첫열 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
        #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
        #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: #삽입(왼쪽), 삭제(위쪽), 교체 (왼쪽 위) 중에서 최소 비용
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))


# 리벤 슈테인 알고리즘

# 러시아 과학자 블라디미르 리벤슈테인(Vladimir Levenshtein)가 고안한 알고리즘입니다. 편집 거리(Edit Distance) 라는 이름으로도 불립니다.

# Levenshtein Distance는 두 개의 문자열 A, B가 주어졌을 때 두 문자열이 얼마나 유사한 지를 알아낼 수 있는 알고리즘입니다.

# 그러니까, 문자열 A가 문자열 B와 같아지기 위해서는 몇 번의 연산을 진행해야 하는 지 계산할 수 있습니다.