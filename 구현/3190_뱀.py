from collections import deque

# 2 <= N <= 100
board = [[0 for _ in range(102) for row in range(102)]]

# 확인을 위한 함수 board 크기만큼 프린트
def print_board(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(board[i][j], end= '')

        print()

def solution(n, apples, k, moves):
    for i in range(len(apples)):
        # apple을 board에 1로 설정
        y = apples[i][0]
        x = apples[i][1]
        board[y][x] = 1
    # 시간
    sec = 1
    # 현재 y,x 좌표
    y, x = 1, 1
    # 출발점
    board[1][1] = 2
    # moves의 index
    mov = 0
    # x,y 이동좌표
    signs = [[0,1],[1,0],[0,-1],[-1,0]] 
    # 방향전환
    vec = 0
    # 뱀의 몸 좌표
    body = deque([[1,1]])

    while (1):
        # y, x 좌표이동
        y = y + signs[vec][0]
        x = x + signs[vec][1]
        

        if (y > n or x > n or y < 1 or x < 1): #board가 범위를 벗어날때
            print(sec)
            return
        
        if (board[y][x] == 2): # 몸이 겹칠때
            print(sec)
            return

        if board[y][x] != 1: # apple이 아닐때 꼬리 컷
            tmp = body.popleft()
            board[int(tmp[0])][int(tmp[1])] = 0 # 빈공간을 ㅗ초기화
        
        body.append([y,x])
        board[y][x] = 2

        if (mov < k and moves[mov][0] == sec): # 방향전환
            if (moves[mov][1] == 'D'): # 'D' 일 경우 오른쪽
                vec += 1
                # 아니면 왼쪽으로 돌기
            else:
                vec -= 1
            vec %= 4
            mov += 1

        sec += 1

n = int(input())
k = int(input())

apples, moves = [], []

for i in range(k):
    a,b = map(int,input().split())
    apples.append([a,b])

k = int(input())

for j in range(k):
    a,b= input().split()
    moves.append([int(a),b])

solution(n,apples,k,moves)

# solution(6, [[3,4],[2,5],[5,3]],[[3,'D'],[15,'L'],[17,'D']])