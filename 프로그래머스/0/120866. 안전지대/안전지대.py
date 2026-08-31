def solution(board):
    answer = 0
    # 닿는 곳은 다 +1 으로 바꾸기
    n = len(board)
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    visited = [[0] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                for i in range(len(dx)):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < n and 0 <= ny < n :
                        visited[nx][ny] = 1
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                answer += 1
                        
                    
    return answer