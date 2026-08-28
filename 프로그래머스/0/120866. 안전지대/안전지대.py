def solution(board):
    answer = 0
    # 닿는 곳은 모두 폭파 지역 
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    n = len(board)
    a_list = [[0] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            
            if board[x][y] == 1:
                for i in range(len(dx)):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n :
                        a_list[nx][ny] = 1
                    
    for x in range(n):
        for y in range(n):
            if not a_list[x][y]:
                answer += 1
    return answer