def solution(board):
    answer = 0
    
    # 지뢰이면 주위 1로 바꿈
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    
    for x in range(n):
        for y in range(n):
            if board[x][y]  == 1:
                for i in range(len(dx)):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                        visited[nx][ny] = 1
    
    for x in range(n):
        for y in range(n):
            if not visited[x][y] :
                answer += 1
    return answer