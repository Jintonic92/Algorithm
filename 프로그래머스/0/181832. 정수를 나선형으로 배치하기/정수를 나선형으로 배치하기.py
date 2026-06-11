def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    idx = 0 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for cnt in range(1, n**2+1):
        answer[x][y] = cnt 
        
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx >= n or n < 0 or ny >= n or n < 0 or answer[nx][ny] != 0:
            idx = (idx + 1) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]
        
        x = nx
        y = ny
        
    return answer