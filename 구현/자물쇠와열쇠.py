# 2차원 배열 90도 회전 메소드
def rotate_by_90deg(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_matrix[j][n-1-i] = matrix[i][j]
            
    return new_matrix
    
# 3배x3배로 확장된 자물쇠의 가운데 부분 (original 자물쇠)이
# 모두 1인지 (i.e. 열쇠가 맞는 지) 확인
def check(new_lock):
    n = len(new_lock) // 3
    
    for i in range(n, n * 2):
    	for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True
    
# 메인 solution
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 3배 x 3배로 자물쇠 초기화
    new_lock = [[0] * (n * 3) for _ in range(n*3)]
    
    # 새로운 자물쇠 중간 부분에 기존 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j] 
            
    # 열쇠가 맞는 지 체크 - 모든 방향에 대해
    for _ in range(4):
        key = rotate_by_90deg(key)
        for x in range(n*2):
            for y in range(n*2):
                # 열쇠 끼워보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 맞는 지 검사
                if check(new_lock):
                    return True
                    
                # 안 맞으면 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                
    return False