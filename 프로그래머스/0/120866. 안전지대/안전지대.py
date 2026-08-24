def solution(board):
    answer = 0
    # 닿는 곳 1로 바꾸기
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    
    visited = [[0] * len(board) for _ in range(len(board))]
    n = len(board)
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for i in range(len(dx)):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = 1
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                answer += 1 
                
    return answer