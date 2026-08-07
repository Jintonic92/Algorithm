def solution(board):
    answer = 0
    # 지뢰를 먼저 찾아서 주위를 다 1로 만들기 
    # 그리고 전체 돌면서 0인 지역 찾기 
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    
    # 방향키
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                visited[x][y] = 1
                for i in range(len(dx)):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        visited[nx][ny] = 1
    
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                answer += 1
    
    return answer